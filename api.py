from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import os
from structured_crawl import StructuredCrawler

app = FastAPI(title="CRAWL4AI-PROJECT API")

class CrawlRequest(BaseModel):
    urls: List[str]
    max_pages: Optional[int] = 100
    exclude_external_links: Optional[bool] = True
    exclude_social_media_links: Optional[bool] = True
    exclude_domains: Optional[List[str]] = None
    output_dir: Optional[str] = "crawled_docs"

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "CRAWL4AI-PROJECT"}

@app.post("/crawl")
async def crawl_websites(request: CrawlRequest):
    """Crawl websites and extract structured content"""
    try:
        os.makedirs(request.output_dir, exist_ok=True)
        
        crawler = StructuredCrawler(
            exclude_external_links=request.exclude_external_links,
            exclude_social_media_links=request.exclude_social_media_links,
            exclude_domains=request.exclude_domains
        )
        
        results = []
        content_data = []

        for url in request.urls:
            try:
                # Crawl and extract structured data
                site_content = await crawler.crawl_website(
                    url, 
                    max_pages=request.max_pages
                )
                
                content_data.extend(site_content)
                results.append({
                    "url": url,
                    "status": "completed",
                    "success": True,
                    "articles_processed": len(site_content)
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
            "content": content_data,
            "output_directory": os.path.abspath(request.output_dir)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))