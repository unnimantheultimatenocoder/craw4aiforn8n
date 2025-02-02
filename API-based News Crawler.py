import requests
import json
import time
from typing import List, Dict

class NewsCrawler:
    def __init__(self, base_url: str = "http://localhost:11235"):
        self.base_url = base_url
        
    def crawl_websites(self, urls: List[str]) -> List[Dict]:
        results = []
        
        for url in urls:
            print(f"Crawling: {url}")
            
            # Prepare the crawl request
            request_data = {
                "urls": url,
                "priority": 10,
                "cache_mode": "enabled",
                "crawler_params": {
                    "headless": True,
                    "wait_for": "article",  # Wait for article content to load
                    "word_count_threshold": 100  # Only get substantial content
                }
            }
            
            try:
                # Make the API call
                response = requests.post(
                    f"{self.base_url}/crawl_direct",
                    json=request_data
                )
                response.raise_for_status()
                
                result = response.json()
                
                if result["result"]["success"]:
                    content = {
                        "url": url,
                        "content": result["result"]["markdown"],
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    results.append(content)
                    print(f"Successfully crawled {url}")
                else:
                    print(f"Failed to crawl {url}: {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"Error crawling {url}: {str(e)}")
                
            # Be nice to servers
            time.sleep(2)
            
        return results

# Example usage
if __name__ == "__main__":
    crawler = NewsCrawler()
    urls = [
        "https://www.bbc.com/news",
        "https://edition.cnn.com/"
    ]
    results = crawler.crawl_websites(urls)
    
    # Save results to file
    with open("crawled_news.json", "w") as f:
        json.dump(results, f, indent=2)