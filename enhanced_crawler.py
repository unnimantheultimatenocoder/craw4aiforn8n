import asyncio
import os
import base64
from typing import List, Optional, Dict, Any
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
import aiohttp
from dataclasses import dataclass
import time

@dataclass
class CrawlResult:
    """Store crawling results including media information"""
    url: str
    success: bool
    markdown: Optional[str] = None
    media: Optional[Dict[str, List[Dict[str, Any]]]] = None
    screenshot: Optional[str] = None
    error_message: Optional[str] = None

async def download_image(session: aiohttp.ClientSession, url: str, output_dir: str, img_info: dict) -> Optional[str]:
    """Downloads image and saves it with metadata"""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                # Create images directory
                images_dir = os.path.join(output_dir, 'images')
                os.makedirs(images_dir, exist_ok=True)
                
                # Generate filename from URL or use timestamp
                filename = os.path.basename(urlparse(url).path)
                if not filename or '.' not in filename:
                    timestamp = int(time.time() * 1000)
                    filename = f"image_{timestamp}.png"
                
                filepath = os.path.join(images_dir, filename)
                
                # Save image
                with open(filepath, 'wb') as f:
                    f.write(await response.read())
                
                # Save metadata alongside image
                metadata_path = os.path.join(images_dir, f"{os.path.splitext(filename)[0]}_metadata.txt")
                with open(metadata_path, 'w', encoding='utf-8') as f:
                    f.write(f"Original URL: {url}\n")
                    f.write(f"Alt Text: {img_info.get('alt', 'N/A')}\n")
                    f.write(f"Description: {img_info.get('desc', 'N/A')}\n")
                    f.write(f"Score: {img_info.get('score', 'N/A')}\n")
                    f.write(f"Width: {img_info.get('width', 'N/A')}\n")
                    f.write(f"Height: {img_info.get('height', 'N/A')}\n")
                
                return filepath
    except Exception as e:
        print(f"Error downloading image {url}: {e}")
    return None

async def save_screenshot(screenshot_data: str, output_dir: str, page_name: str) -> Optional[str]:
    """Saves page screenshot"""
    try:
        screenshots_dir = os.path.join(output_dir, 'screenshots')
        os.makedirs(screenshots_dir, exist_ok=True)
        
        filepath = os.path.join(screenshots_dir, f"{page_name}_screenshot.png")
        
        # Handle both base64 and binary screenshot data
        if isinstance(screenshot_data, str) and screenshot_data.startswith('data:image'):
            # Base64 encoded screenshot
            try:
                img_data = base64.b64decode(screenshot_data.split(',')[1])
                with open(filepath, 'wb') as f:
                    f.write(img_data)
                return filepath
            except Exception as e:
                print(f"Error decoding base64 screenshot: {e}")
        else:
            # Binary screenshot data
            with open(filepath, 'wb') as f:
                f.write(screenshot_data)
            return filepath
    except Exception as e:
        print(f"Error saving screenshot: {e}")
    return None

async def crawl_url_with_media(url: str, output_dir: str = "crawled_content") -> CrawlResult:
    """Crawls a single URL with enhanced image and screenshot support"""
    browser_config = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    
    # Configure crawler with focus on images
    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(),
        wait_for_images=True,  # Wait for images to load
        exclude_external_images=False,  # Include all images
        screenshot=True  # Enable screenshot capture
    )
    
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()
    
    try:
        session_id = f"session_{urlparse(url).netloc}"
        result = await crawler.arun(
            url=url,
            config=crawl_config,
            session_id=session_id
        )
        
        if result.success:
            # Create output directories
            os.makedirs(output_dir, exist_ok=True)
            
            # Save markdown content
            parsed_url = urlparse(url)
            page_name = parsed_url.path.strip('/').replace('/', '_') or 'index'
            markdown_path = os.path.join(output_dir, f"{page_name}.md")
            with open(markdown_path, 'w', encoding='utf-8') as f:
                f.write(result.markdown_v2.raw_markdown)
            
            # Process images
            if result.media and 'images' in result.media:
                async with aiohttp.ClientSession() as session:
                    print("\nProcessing images:")
                    for i, img in enumerate(result.media['images']):
                        if 'src' in img:
                            print(f"[Image {i+1}] URL: {img['src']}")
                            print(f"           Alt text: {img.get('alt', '')}")
                            print(f"           Score: {img.get('score', 'N/A')}")
                            print(f"           Description: {img.get('desc', '')}\n")
                            
                            absolute_url = urljoin(url, img['src'])
                            local_path = await download_image(
                                session, absolute_url, output_dir, img
                            )
                            if local_path:
                                img['local_path'] = local_path
                                print(f"           Saved to: {local_path}")
            
            # Handle screenshot
            if hasattr(result, 'screenshot') and result.screenshot:
                screenshot_path = await save_screenshot(
                    result.screenshot, output_dir, page_name
                )
                if screenshot_path:
                    print(f"\nSaved page screenshot to: {screenshot_path}")
            
            return CrawlResult(
                url=url,
                success=True,
                markdown=result.markdown_v2.raw_markdown,
                media=result.media,
                screenshot=screenshot_path if 'screenshot_path' in locals() else None
            )
        
        return CrawlResult(
            url=url,
            success=False,
            error_message=result.error_message
        )
    
    finally:
        await crawler.close()

async def crawl_urls_with_media(urls: List[str], output_dir: str = "crawled_content") -> List[CrawlResult]:
    """Crawls multiple URLs sequentially with enhanced image handling"""
    results = []
    for url in urls:
        print(f"\nCrawling: {url}")
        result = await crawl_url_with_media(url, output_dir)
        results.append(result)
        
        if result.success:
            print(f"Success! Content saved to {output_dir}")
            if result.media and 'images' in result.media:
                print(f"Found {len(result.media['images'])} images")
            if result.screenshot:
                print("Screenshot captured successfully")
        else:
            print(f"Failed: {result.error_message}")
    
    return results

async def main():
    # Example URLs - replace with your target URLs
    urls = [
        "https://docs.datastax.com/en/langflow/index.html",
        # Add more URLs as needed
    ]
    
    # Set output directory
    output_dir = "crawled_docs"
    
    # Crawl URLs
    results = await crawl_urls_with_media(urls, output_dir)
    
    # Print summary
    print("\n=== Crawling Summary ===")
    success_count = sum(1 for r in results if r.success)
    print(f"Successfully crawled: {success_count}/{len(results)} URLs")
    
    for result in results:
        if result.success:
            print(f"\nFor {result.url}:")
            if result.media and 'images' in result.media:
                print(f"- Images: {len(result.media['images'])} downloaded")
            if result.screenshot:
                print("- Screenshot: Captured")

if __name__ == "__main__":
    asyncio.run(main())