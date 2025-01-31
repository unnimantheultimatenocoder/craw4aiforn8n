import asyncio
import os
from uuid import uuid4
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import MemoryAdaptiveDispatcher, SemaphoreDispatcher  # Correct import path
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def save_markdown_results(urls):
    # Configure markdown generation
    markdown_generator = DefaultMarkdownGenerator(
        options={"citations": True, "body_width": 80}
    )

    # Set up crawler configuration
    run_config = CrawlerRunConfig(
        cache_mode="bypass",
        markdown_generator=markdown_generator,
        extraction_strategy="auto"
    )

    # Configure dispatcher with correct parameters
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=80.0,
        max_session_permit=10,
        check_interval=1.0,
        rate_limiter=None,
        monitor=None
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        )

        # Process and save results
        for result in results:
            if result.success and result.markdown_v2:
                filename = f"{uuid4().hex}.md"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(result.markdown_v2.markdown_with_citations)
                print(f"Saved: {filename}")
            else:
                print(f"Failed: {result.url} - {result.error_message}")

async def main():
    urls = [
        "https://example.com",
        "https://www.wikipedia.org",
        "https://github.com"
    ]
    
    os.makedirs("markdown_results", exist_ok=True)
    os.chdir("markdown_results")
    
    await save_markdown_results(urls)

if __name__ == "__main__":
    asyncio.run(main())