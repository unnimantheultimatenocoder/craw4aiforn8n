import asyncio
import os
from typing import List, Set
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from bs4 import BeautifulSoup

async def extract_internal_links(crawler: AsyncWebCrawler, base_url: str, config: CrawlerRunConfig) -> Set[str]:
    """
    Extracts internal links from a given URL.
    
    Args:
        crawler: AsyncWebCrawler instance
        base_url: The base URL to crawl
        config: Crawler configuration
    
    Returns:
        Set[str]: Set of internal URLs found
    """
    result = await crawler.arun(url=base_url, config=config)
    if not result.success or not result.html:
        return set()
    
    internal_links = set()
    base_domain = urlparse(base_url).netloc
    
    soup = BeautifulSoup(result.html, 'html.parser')
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Convert relative URLs to absolute
        if not href.startswith(('http://', 'https://')):
            href = urljoin(base_url, href)
        
        # Only include internal links from the same domain
        if urlparse(href).netloc == base_domain:
            internal_links.add(href)
    
    return internal_links

async def crawl_urls(urls: List[str], output_dir: str = "crawled_docs", max_internal_pages: int = 10):
    """
    Crawls URLs and their internal links, saving content as markdown files.
    
    Args:
        urls: List of URLs to crawl
        output_dir: Directory to save markdown files (default: "crawled_docs")
        max_internal_pages: Maximum number of internal pages to crawl per URL
    """
    print("\n=== Starting URL Crawler ===")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving markdown files to: {os.path.abspath(output_dir)}")

    browser_config = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )

    # Create the crawler
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    # Track statistics
    success_count = 0
    failed_count = 0
    total_markdown_size = 0
    processed_urls = set()

    try:
        session_id = "session1"
        
        for base_url in urls:
            if base_url in processed_urls:
                continue
                
            # Process the base URL first
            processed_urls.add(base_url)
            print(f"\nProcessing base URL: {base_url}")
            
            # Crawl the base URL
            result = await crawler.arun(
                url=base_url,
                config=crawl_config,
                session_id=session_id
            )
            
            if result.success:
                success_count += 1
                markdown_length = len(result.markdown_v2.raw_markdown)
                total_markdown_size += markdown_length
                print(f"Successfully crawled: {base_url}")
                print(f"Markdown length: {markdown_length}")
                
                # Save base URL content
                parsed_url = urlparse(base_url)
                filename = parsed_url.path.strip('/').replace('/', '_')
                if not filename:
                    filename = 'index'
                filename = f"{filename}.md"
                
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(result.markdown_v2.raw_markdown)
                print(f"Saved to: {filepath}")
                
                # Extract and process internal links
                internal_links = await extract_internal_links(crawler, base_url, crawl_config)
                print(f"Found {len(internal_links)} internal links")
                
                # Process internal links up to the limit
                for url in list(internal_links)[:max_internal_pages]:
                    if url in processed_urls:
                        continue
                        
                    processed_urls.add(url)
                    print(f"\nProcessing internal link: {url}")
                    
                    result = await crawler.arun(
                        url=url,
                        config=crawl_config,
                        session_id=session_id
                    )
                    
                    if result.success:
                        success_count += 1
                        markdown_length = len(result.markdown_v2.raw_markdown)
                        total_markdown_size += markdown_length
                        print(f"Successfully crawled: {url}")
                        print(f"Markdown length: {markdown_length}")
                        
                        # Save internal link content
                        parsed_url = urlparse(url)
                        filename = parsed_url.path.strip('/').replace('/', '_')
                        if not filename:
                            filename = 'index'
                        filename = f"{filename}.md"
                        
                        filepath = os.path.join(output_dir, filename)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(result.markdown_v2.raw_markdown)
                        print(f"Saved to: {filepath}")
                    else:
                        failed_count += 1
                        print(f"Failed: {url} - Error: {result.error_message}")
            else:
                failed_count += 1
                print(f"Failed: {base_url} - Error: {result.error_message}")
                
    finally:
        await crawler.close()
        
        # Print summary statistics
        print("\n=== Crawling Summary ===")
        print(f"Successfully crawled: {success_count} URLs")
        print(f"Failed: {failed_count} URLs")
        print(f"Total markdown content: {total_markdown_size:,} characters")
        print(f"Output directory: {os.path.abspath(output_dir)}")

async def main():
    """
    Main function to run the crawler.
    """
    output_dir = "crawled_docs"
    
    # List of URLs to crawl
    urls = [
        "https://www.indiatoday.in/education-today/study-abroad"
        
    ]
    
    if urls:
        print(f"Starting crawl with {len(urls)} URLs")
        await crawl_urls(urls, output_dir, max_internal_pages=10)
    else:
        print("No URLs provided to crawl")

if __name__ == "__main__":
    asyncio.run(main())