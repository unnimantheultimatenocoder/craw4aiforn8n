import asyncio
from structured_crawl import StructuredCrawler

async def test_crawler():
    # Initialize crawler with filtering options
    crawler = StructuredCrawler(
        exclude_external_links=True,
        exclude_social_media_links=True,
        exclude_domains=['ads.example.com', 'analytics.example.com']
    )
    
    # Test URL - replace with your target website
    test_url = "https://www.indiatoday.in/education-today/study-abroad"
    
    try:
        # Crawl and get structured data
        results = await crawler.crawl_website(test_url, max_pages=5)
        
        # Print results
        print(f"\nCrawled {len(results)} articles:")
        for idx, article in enumerate(results, 1):
            print(f"\nArticle {idx}:")
            print(f"Title: {article['title'][:100]}...")
            print(f"URL: {article['source_url']}")
            print(f"Timestamp: {article['timestamp']}")
            print(f"Content length: {len(article['content'])} characters")
            
    except Exception as e:
        print(f"Error during crawling: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_crawler())