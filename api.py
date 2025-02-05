from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import asyncio
import os
from multiple_pages import FullSiteCrawler

app = FastAPI(title="CRAWL4AI-PROJECT API")

class CrawlRequest(BaseModel):
    urls: List[str]
    max_pages: Optional[int] = 10
    output_dir: Optional[str] = "crawled_docs"

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "CRAWL4AI-PROJECT"}

@app.post("/crawl")
async def crawl_websites(request: CrawlRequest):
    """Crawl multiple websites asynchronously and return content"""
    try:
        output_dir = request.output_dir
        os.makedirs(output_dir, exist_ok=True)

        crawler = FullSiteCrawler(output_dir=output_dir)
        results = []
        all_data = [] # Added: List to store data for all URLs

        for url in request.urls:
            try:
                await crawler.crawl_website(url, max_pages=request.max_pages)

                # Read content from saved files
                website_dir = os.path.join(output_dir, crawler.domain_name(url))  # Correct directory name
                website_data = []
                for filename in os.listdir(website_dir):
                    if filename.endswith(".txt"):  # Assuming you save as .txt
                        filepath = os.path.join(website_dir, filename)
                        try:
                            with open(filepath, "r", encoding="utf-8") as f:  # Handle encoding
                                content = f.read()
                            website_data.append({"filename": filename, "content": content})
                        except Exception as e:
                            print(f"Error reading file {filename}: {e}") # Log the error

                results.append({
                    "url": url,
                    "status": "completed",
                    "success": True
                })
                all_data.append({"url": url, "data": website_data}) # Append data for this URL
            except Exception as e:
                results.append({
                    "url": url,
                    "status": "failed",
                    "error": str(e),
                    "success": False
                })

        return {
            "status": "completed",
            "results": results,
            "data": all_data,  # Return the crawled data
            "output_directory": os.path.abspath(output_dir)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))