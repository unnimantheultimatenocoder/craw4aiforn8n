import asyncio
import os
from typing import List
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
import requests
from xml.etree import ElementTree

async def crawl_sequential(urls: List[str], output_dir: str = "crawled_docs"):
    """
    Crawls URLs sequentially and saves markdown content to files.
    
    Args:
        urls: List of URLs to crawl
        output_dir: Directory to save markdown files (default: "crawled_docs")
    """
    print("\n=== Sequential Crawling with Session Reuse ===")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving markdown files to: {os.path.abspath(output_dir)}")

    browser_config = BrowserConfig(
        headless=True,
        # For better performance in Docker or low-memory environments:
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )

    # Create the crawler (opens the browser)
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    # Track statistics
    success_count = 0
    failed_count = 0
    total_markdown_size = 0

    try:
        session_id = "session1"  # Reuse the same session across all URLs
        for url in urls:
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
                
                # Create filename from URL
                parsed_url = urlparse(url)
                filename = parsed_url.path.strip('/').replace('/', '_')
                if not filename:
                    filename = 'index'
                filename = f"{filename}.md"
                
                # Save to file
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(result.markdown_v2.raw_markdown)
                print(f"Saved to: {filepath}\n")
            else:
                failed_count += 1
                print(f"Failed: {url} - Error: {result.error_message}\n")
                
    finally:
        # After all URLs are done, close the crawler (and the browser)
        await crawler.close()
        
        # Print summary statistics
        print("\n=== Crawling Summary ===")
        print(f"Successfully crawled: {success_count} URLs")
        print(f"Failed: {failed_count} URLs")
        print(f"Total markdown content: {total_markdown_size:,} characters")
        print(f"Output directory: {os.path.abspath(output_dir)}")

def get_pydantic_ai_docs_urls():
    """
    Fetches all URLs from the Pydantic AI documentation sitemap.
    
    Returns:
        List[str]: List of URLs from the sitemap
    """            
    sitemap_url = "https://docs.langflow.org/sitemap.xml"
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse the XML
        root = ElementTree.fromstring(response.content)
        
        # Extract all URLs from the sitemap
        # The namespace is usually defined in the root element
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

async def main():
    """
    Main function to run the crawler.
    Gets URLs from sitemap and initiates crawling.
    """
    # You can customize the output directory here
    output_dir = "crawled_docs"
    
    urls = get_pydantic_ai_docs_urls()
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        await crawl_sequential(urls, output_dir)
    else:
        print("No URLs found to crawl")

if __name__ == "__main__":
    asyncio.run(main())