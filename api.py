from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from urllib.parse import urlparse
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
    """Crawl multiple websites asynchronously and return content"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(request.output_dir, exist_ok=True)
        
        crawler = FullSiteCrawler(output_dir=request.output_dir)
        results = []
        content_data = []

        for url in request.urls:
            try:
                # Crawl the website
                await crawler.crawl_website(url, max_pages=request.max_pages)
                
                # Get domain folder name
                domain = urlparse(url).netloc.replace('.', '_')
                site_dir = os.path.join(request.output_dir, domain)
                
                # Read all markdown files in the directory
                site_content = []
                if os.path.exists(site_dir):
                    for filename in os.listdir(site_dir):
                        if filename.endswith('.md'):
                            file_path = os.path.join(site_dir, filename)
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    site_content.append({
                                        'url': url,
                                        'filename': filename,
                                        'content': content
                                    })
                            except Exception as e:
                                print(f"Error reading file {filename}: {str(e)}")
                
                content_data.extend(site_content)
                results.append({
                    "url": url,
                    "status": "completed",
                    "success": True,
                    "files_processed": len(site_content)
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