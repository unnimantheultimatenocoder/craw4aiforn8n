[Crawl4AI Documentation (v0.4.3bx)](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/lazy-loading/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/lazy-loading/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/lazy-loading/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/lazy-loading/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/lazy-loading/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/lazy-loading/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/lazy-loading/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/lazy-loading/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/lazy-loading/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/lazy-loading/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/lazy-loading/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/lazy-loading/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/lazy-loading/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/lazy-loading/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/lazy-loading/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/lazy-loading/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/lazy-loading/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/lazy-loading/<../file-downloading/>)
    * Lazy Loading
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/lazy-loading/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/lazy-loading/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/lazy-loading/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/lazy-loading/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/lazy-loading/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/lazy-loading/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/lazy-loading/api/arun/>)
    * [arun_many()](https://docs.crawl4ai.com/advanced/lazy-loading/api/arun_many/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/lazy-loading/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/lazy-loading/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/api/strategies/>)


  * [Handling Lazy-Loaded Images](https://docs.crawl4ai.com/advanced/lazy-loading/<#handling-lazy-loaded-images>)
  * [Example: Ensuring Lazy Images Appear](https://docs.crawl4ai.com/advanced/lazy-loading/<#example-ensuring-lazy-images-appear>)
  * [Combining with Other Link & Media Filters](https://docs.crawl4ai.com/advanced/lazy-loading/<#combining-with-other-link-media-filters>)
  * [Tips & Troubleshooting](https://docs.crawl4ai.com/advanced/lazy-loading/<#tips-troubleshooting>)


## Handling Lazy-Loaded Images
Many websites now load images **lazily** as you scroll. If you need to ensure they appear in your final crawl (and in `result.media`), consider:
1. **`wait_for_images=True`**– Wait for images to fully load. 2.**`scan_full_page`**– Force the crawler to scroll the entire page, triggering lazy loads. 3.**`scroll_delay`**– Add small delays between scroll steps.
**Note** : If the site requires multiple “Load More” triggers or complex interactions, see the [Page Interaction docs](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>).
### Example: Ensuring Lazy Images Appear
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
from crawl4ai.async_configs import CacheMode
async def main():
  config = CrawlerRunConfig(
    # Force the crawler to wait until images are fully loaded
    wait_for_images=True,
    # Option 1: If you want to automatically scroll the page to load images
    scan_full_page=True, # Tells the crawler to try scrolling the entire page
    scroll_delay=0.5,   # Delay (seconds) between scroll steps
    # Option 2: If the site uses a 'Load More' or JS triggers for images,
    # you can also specify js_code or wait_for logic here.
    cache_mode=CacheMode.BYPASS,
    verbose=True
  )
  async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
    result = await crawler.arun("https://www.example.com/gallery", config=config)
    if result.success:
      images = result.media.get("images", [])
      print("Images found:", len(images))
      for i, img in enumerate(images[:5]):
        print(f"[Image {i}] URL: {img['src']}, Score: {img.get('score','N/A')}")
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Explanation** :
  * **`wait_for_images=True`**The crawler tries to ensure images have finished loading before finalizing the HTML.
  * **`scan_full_page=True`**Tells the crawler to attempt scrolling from top to bottom. Each scroll step helps trigger lazy loading.
  * **`scroll_delay=0.5`**Pause half a second between each scroll step. Helps the site load images before continuing.


**When to Use** :
  * **Lazy-Loading** : If images appear only when the user scrolls into view, `scan_full_page` + `scroll_delay` helps the crawler see them. 
  * **Heavier Pages** : If a page is extremely long, be mindful that scanning the entire page can be slow. Adjust `scroll_delay` or the max scroll steps as needed.


## Combining with Other Link & Media Filters
You can still combine **lazy-load** logic with the usual **exclude_external_images** , **exclude_domains** , or link filtration:
```
config = CrawlerRunConfig(
  wait_for_images=True,
  scan_full_page=True,
  scroll_delay=0.5,
  # Filter out external images if you only want local ones
  exclude_external_images=True,
  # Exclude certain domains for links
  exclude_domains=["spammycdn.com"],
)

```

This approach ensures you see **all** images from the main domain while ignoring external ones, and the crawler physically scrolls the entire page so that lazy-loading triggers.
## Tips & Troubleshooting
1. **Long Pages** - Setting `scan_full_page=True` on extremely long or infinite-scroll pages can be resource-intensive. - Consider using [hooks](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>) or specialized logic to load specific sections or “Load More” triggers repeatedly.
2. **Mixed Image Behavior** - Some sites load images in batches as you scroll. If you’re missing images, increase your `scroll_delay` or call multiple partial scrolls in a loop with JS code or hooks.
3. **Combining with Dynamic Wait** - If the site has a placeholder that only changes to a real image after a certain event, you might do `wait_for="css:img.loaded"` or a custom JS `wait_for`.
4. **Caching** - If `cache_mode` is enabled, repeated crawls might skip some network fetches. If you suspect caching is missing new images, set `cache_mode=CacheMode.BYPASS` for fresh fetches.
With **lazy-loading** support, **wait_for_images** , and **scan_full_page** settings, you can capture the entire gallery or feed of images you expect—even if the site only loads them as the user scrolls. Combine these with the standard media filtering and domain exclusion for a complete link & media handling strategy.
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/lazy-loading/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching
