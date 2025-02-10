from bs4 import BeautifulSoup
import asyncio
from urllib.parse import urljoin, urlparse
import aiohttp
from datetime import datetime
from typing import List, Dict, Set
import re

class StructuredCrawler:
    def __init__(self, exclude_external_links: bool = True,
                 exclude_social_media_links: bool = True,
                 exclude_domains: List[str] = None):
        self.exclude_external_links = exclude_external_links
        self.exclude_social_media_links = exclude_social_media_links
        self.exclude_domains = set(exclude_domains or [])
        self.visited_urls: Set[str] = set()
        self.social_media_patterns = [
            r'facebook\.com', r'twitter\.com', r'linkedin\.com',
            r'instagram\.com', r'youtube\.com', r'tiktok\.com'
        ]

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

    async def crawl_website(self, start_url: str, max_pages: int = 100) -> List[Dict]:
        """Crawl website and extract structured data from all valid pages."""
        base_domain = urlparse(start_url).netloc
        results = []
        to_visit = {start_url}
        
        async with aiohttp.ClientSession() as session:
            while to_visit and len(self.visited_urls) < max_pages:
                url = to_visit.pop()
                if url in self.visited_urls:
                    continue
                
                self.visited_urls.add(url)
                html_content, error = await self._fetch_url(session, url)
                
                if error:
                    print(f"Error fetching {url}: {error}")
                    continue

                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract data if page looks like an article
                if soup.find('article') or soup.find('main'):
                    article_data = self._extract_article_data(soup, url)
                    results.append(article_data)

                # Find and add new URLs to visit
                for link in soup.find_all('a', href=True):
                    new_url = urljoin(url, link['href'])
                    if (new_url not in self.visited_urls and 
                        new_url not in to_visit and 
                        self._is_valid_url(new_url, base_domain)):
                        to_visit.add(new_url)

        return results