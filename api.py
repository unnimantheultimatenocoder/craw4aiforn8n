from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import os
from multiple_pages import FullSiteCrawler

app = FastAPI(title="CRAWL4AI-PROJECT API")

class CrawlRequest(BaseModel):
    urls: List[str]
    max_pages: Optional[int] = 100
    output_dir: Optional[str] = "crawled_docs"

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "CRAWL4AI-PROJECT"}

@app.post("/crawl")
async def crawl_websites(request: CrawlRequest):
    """Crawl multiple websites asynchronously"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(request.output_dir, exist_ok=True)
        
        crawler = FullSiteCrawler(output_dir=request.output_dir)
        results = []

        for url in request.urls:
            try:
                await crawler.crawl_website(url, max_pages=request.max_pages)
                results.append({
                    "url": url,
                    "status": "completed",
                    "success": True
                })
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
            "output_directory": os.path.abspath(request.output_dir)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))