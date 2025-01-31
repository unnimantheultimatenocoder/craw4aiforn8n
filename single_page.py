import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://claude.ai/chat/b965fd82-24bf-4628-85e8-4bb37bff24a2",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())