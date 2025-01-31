import asyncio
import os
from typing import List, Set
from datetime import datetime
from urllib.parse import urlparse, urljoin
import aiohttp
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

class FullSiteCrawler:
    def __init__(self, output_dir: str = "crawled_sites"):
        self.output_dir = output_dir
        self.browser_config = BrowserConfig(
            headless=True,
            extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
        )
        self.crawl_config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator()
        )
        
    def is_valid_url(self, url: str, base_domain: str) -> bool:
        """
        Checks if a URL is valid and belongs to the same domain.
        
        Args:
            url: URL to check
            base_domain: Domain to compare against
            
        Returns:
            bool: True if URL is valid and belongs to base domain
        """
        try:
            parsed = urlparse(url)
            return (
                bool(parsed.netloc) and
                parsed.netloc == base_domain and
                parsed.scheme in ['http', 'https'] and
                not any(ext in url.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip'])
            )
        except:
            return False

    async def discover_links(self, url: str, base_domain: str) -> Set[str]:
        """
        Discovers all links on a page belonging to the same domain.
        
        Args:
            url: URL to scan for links
            base_domain: Domain to filter links
            
        Returns:
            Set of discovered URLs
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        
                        links = set()
                        for anchor in soup.find_all('a', href=True):
                            href = anchor['href']
                            full_url = urljoin(url, href)
                            
                            if self.is_valid_url(full_url, base_domain):
                                links.add(full_url)
                        
                        return links
                    return set()
        except Exception as e:
            print(f"Error discovering links on {url}: {str(e)}")
            return set()

    async def crawl_website(self, base_url: str, max_pages: int = 100):
        """
        Crawls an entire website up to max_pages.
        
        Args:
            base_url: Starting URL for the crawl
            max_pages: Maximum number of pages to crawl
        """
        print(f"\n=== Starting full crawl of {base_url} ===")
        
        # Create website-specific output directory
        base_domain = urlparse(base_url).netloc
        site_folder = base_domain.replace('.', '_')
        site_output_dir = os.path.join(self.output_dir, site_folder)
        os.makedirs(site_output_dir, exist_ok=True)
        
        # Initialize crawler
        crawler = AsyncWebCrawler(config=self.browser_config)
        await crawler.start()
        
        try:
            # Track URLs
            crawled_urls = set()
            to_crawl = {base_url}
            
            session_id = f"session_{site_folder}"
            
            while to_crawl and len(crawled_urls) < max_pages:
                current_url = to_crawl.pop()
                
                if current_url in crawled_urls:
                    continue
                
                # Crawl the page
                result = await crawler.arun(
                    url=current_url,
                    config=self.crawl_config,
                    session_id=session_id
                )
                
                if result.success:
                    # Save the content
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    parsed_url = urlparse(current_url)
                    path_part = parsed_url.path.strip('/').replace('/', '_')
                    if not path_part:
                        path_part = 'index'
                    filename = f"{path_part}_{timestamp}.md"
                    
                    filepath = os.path.join(site_output_dir, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(result.markdown_v2.raw_markdown)
                    
                    print(f"Crawled ({len(crawled_urls) + 1}/{max_pages}): {current_url}")
                    
                    # Discover new links
                    new_links = await self.discover_links(current_url, base_domain)
                    to_crawl.update(new_links - crawled_urls)
                    
                    # Mark as crawled
                    crawled_urls.add(current_url)
                    
                    # Add a small delay to be nice to the server
                    await asyncio.sleep(1)
                else:
                    print(f"Failed to crawl {current_url}: {result.error_message}")
            
            print(f"\nCrawl complete for {base_url}")
            print(f"Total pages crawled: {len(crawled_urls)}")
            print(f"Content saved in: {os.path.abspath(site_output_dir)}")
                    
        finally:
            await crawler.close()

async def main():
    # List of websites to crawl
    websites = [
        "https://www.bbc.com/news",  # Replace with actual website URL
        "https://edition.cnn.com/"  # Replace with actual website URL
    ]
    
    crawler = FullSiteCrawler(output_dir="full_sites")
    
    # Crawl each website
    for website in websites:
        await crawler.crawl_website(website, max_pages=100)  # Adjust max_pages as needed

if __name__ == "__main__":
    asyncio.run(main())