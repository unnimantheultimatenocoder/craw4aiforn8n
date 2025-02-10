from bs4 import BeautifulSoup
import asyncio
from urllib.parse import urljoin, urlparse
import aiohttp
from datetime import datetime
from typing import List, Dict, Set
import re
import json
import os
import logging

class StructuredCrawler:
    def __init__(self, 
                 output_dir: str = "crawled_content",
                 exclude_external_links: bool = True,
                 exclude_social_media_links: bool = True,
                 exclude_domains: List[str] = None):
        self.output_dir = output_dir
        self.exclude_external_links = exclude_external_links
        self.exclude_social_media_links = exclude_social_media_links
        self.exclude_domains = set(exclude_domains or [])
        self.visited_urls: Set[str] = set()
        self.social_media_patterns = [
            r'facebook\.com', r'twitter\.com', r'linkedin\.com',
            r'instagram\.com', r'youtube\.com', r'tiktok\.com'
        ]
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)

    def _is_valid_url(self, url: str, base_domain: str) -> bool:
        """Check if URL should be crawled based on filtering rules."""
        parsed_url = urlparse(url)
        
        # Skip if no domain
        if not parsed_url.netloc:
            return False

        # Check for excluded domains
        if parsed_url.netloc in self.exclude_domains:
            return False

        # Check for social media links
        if self.exclude_social_media_links:
            if any(re.search(pattern, url.lower()) for pattern in self.social_media_patterns):
                return False

        # Check for external links
        if self.exclude_external_links and parsed_url.netloc != base_domain:
            return False

        return True

    def _extract_article_data(self, soup: BeautifulSoup, url: str) -> Dict:
        """Extract structured data from article page."""
        # Title extraction - try multiple common selectors
        title = None
        title_selectors = ['h1', 'article h1', '.article-title', '.post-title']
        for selector in title_selectors:
            title_elem = soup.select_one(selector)
            if title_elem:
                title = title_elem.get_text(strip=True)
                break

        # Content extraction - try multiple common selectors
        content = ""
        content_selectors = ['article', '.article-content', '.post-content', 'main']
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                # Remove unwanted elements
                for unwanted in content_elem.select('script, style, nav, header, footer'):
                    unwanted.decompose()
                content = content_elem.get_text(strip=True, separator=' ')
                break

        # Timestamp extraction - try multiple common selectors and formats
        timestamp = None
        time_selectors = ['time', '.published', '.post-date', 'meta[property="article:published_time"]']
        for selector in time_selectors:
            time_elem = soup.select_one(selector)
            if time_elem:
                timestamp = time_elem.get('datetime', time_elem.get_text(strip=True))
                break

        return {
            "title": title or "No title found",
            "content": content or "No content found",
            "timestamp": timestamp or datetime.now().isoformat(),
            "source_url": url
        }

    async def _fetch_url(self, session: aiohttp.ClientSession, url: str) -> tuple:
        """Fetch URL content with error handling."""
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text(), None
                return None, f"HTTP {response.status}"
        except Exception as e:
            return None, str(e)

    def save_results(self, results: List[Dict], domain: str):
        """Save crawled results to JSON file."""
        if not results:
            return
        
        # Create domain-specific directory
        domain_dir = os.path.join(self.output_dir, domain.replace('.', '_'))
        os.makedirs(domain_dir, exist_ok=True)
        
        # Generate timestamp for filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"crawl_results_{timestamp}.json"
        filepath = os.path.join(domain_dir, filename)
        
        # Save results to JSON file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"Saved {len(results)} articles to {filepath}")
        return filepath

    async def crawl_website(self, start_url: str, max_pages: int = 100) -> List[Dict]:
        """Crawl website and extract structured data from all valid pages."""
        base_domain = urlparse(start_url).netloc
        self.logger.info(f"Starting crawl of {start_url}")
        
        results = []
        to_visit = {start_url}
        
        async with aiohttp.ClientSession() as session:
            while to_visit and len(self.visited_urls) < max_pages:
                url = to_visit.pop()
                if url in self.visited_urls:
                    continue
                
                self.visited_urls.add(url)
                self.logger.info(f"Crawling: {url}")
                
                html_content, error = await self._fetch_url(session, url)
                
                if error:
                    self.logger.error(f"Error fetching {url}: {error}")
                    continue

                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract data if page looks like an article
                if soup.find('article') or soup.find('main'):
                    article_data = self._extract_article_data(soup, url)
                    results.append(article_data)
                    self.logger.info(f"Extracted article: {article_data['title'][:50]}...")

                # Find and add new URLs to visit
                for link in soup.find_all('a', href=True):
                    new_url = urljoin(url, link['href'])
                    if (new_url not in self.visited_urls and 
                        new_url not in to_visit and 
                        self._is_valid_url(new_url, base_domain)):
                        to_visit.add(new_url)
        
        # Save results to file
        saved_file = self.save_results(results, base_domain)
        self.logger.info(f"Crawl completed. Processed {len(self.visited_urls)} pages, found {len(results)} articles")
        
        return results

# This allows the file to be run directly from VS Code
async def main():
    # Example usage
    crawler = StructuredCrawler(
        output_dir="crawled_content",
        exclude_external_links=True,
        exclude_social_media_links=True,
        exclude_domains=['ads.example.com']
    )
    
    # Example URL - replace with your target website
    url = "https://www.indiatoday.in/education-today/study-abroad"
    
    try:
        results = await crawler.crawl_website(url, max_pages=10)
        print(f"\nCrawl Summary:")
        print(f"Total pages crawled: {len(crawler.visited_urls)}")
        print(f"Articles found: {len(results)}")
        print(f"Results saved in: {crawler.output_dir}")
        
    except Exception as e:
        print(f"Error during crawling: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())