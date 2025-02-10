import asyncio
import os
import json
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

class NewsItem(BaseModel):
    """Pydantic model for storing processed news items"""
    title: str = Field(..., description="SEO-friendly title of the news article")
    summary: str = Field(..., description="60-word summary of the article")
    category: str = Field(..., description="Category (education/scholarships/courses/immigration)")
    source_url: str = Field(..., description="Original article URL")
    timestamp: str = Field(..., description="Timestamp of processing")

class NewsProcessor:
    def __init__(self, output_dir: str = "crawled_news"):
        self.raw_dir = os.path.join(output_dir, "raw")
        self.processed_dir = os.path.join(output_dir, "processed")
        
        # Create output directories
        os.makedirs(self.raw_dir, exist_ok=True)
        os.makedirs(self.processed_dir, exist_ok=True)
        
        # Configure browser settings
        self.browser_config = BrowserConfig(
            headless=True,
            extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
        )
        
        # Configure LLM extraction strategy
        self.llm_strategy = LLMExtractionStrategy(
            provider="google/gemini-pro",
            api_token=os.getenv('AIzaSyDOhOPO5rT3PbCZetfa5kbxw3BjXBO8VxQ'),
            schema=NewsItem.model_json_schema(),
            extraction_type="schema",
            instruction="""
            Analyze the content and extract news articles related to education, scholarships, courses, or immigration.
            For each relevant article, create a JSON object with these exact fields:
            {
                "title": "SEO-friendly title",
                "summary": "60-word summary",
                "category": "one of: education/scholarships/courses/immigration",
                "source_url": "article URL",
                "timestamp": "current timestamp"
            }
            
            Return an array of these objects, only including articles that explicitly relate to the categories.
            Format the response as a valid JSON array.
            """,
            chunk_token_threshold=2000,
            overlap_rate=0.1,
            apply_chunking=True,
            input_format="markdown",
            extra_args={"temperature": 0.2, "max_tokens": 1500}
        )
        
        # Configure crawler
        self.crawl_config = CrawlerRunConfig(
            markdown_generator=DefaultMarkdownGenerator(),
            extraction_strategy=self.llm_strategy,
            exclude_external_links=True,
            exclude_social_media_links=True,
            exclude_domains=[
                "facebook.com", "twitter.com", "instagram.com",
                "linkedin.com", "youtube.com", "tiktok.com"
            ]
        )

    def parse_llm_output(self, content: str) -> List[dict]:
        """
        Parse and validate LLM output
        
        Args:
            content: Raw content from LLM
            
        Returns:
            List of validated dictionary items
        """
        try:
            # First, try to parse as JSON
            if isinstance(content, str):
                try:
                    parsed_content = json.loads(content)
                except json.JSONDecodeError as e:
                    print(f"JSON parsing error: {str(e)}")
                    # Try to clean the string and parse again
                    cleaned_content = content.strip()
                    if cleaned_content.startswith("[") and cleaned_content.endswith("]"):
                        try:
                            parsed_content = json.loads(cleaned_content)
                        except json.JSONDecodeError:
                            raise ValueError("Unable to parse LLM output as JSON")
                    else:
                        raise ValueError("Invalid JSON format")
            else:
                parsed_content = content

            # Ensure we have a list
            if not isinstance(parsed_content, list):
                parsed_content = [parsed_content]

            return parsed_content

        except Exception as e:
            print(f"Error parsing LLM output: {str(e)}")
            return []

    async def process_website(self, url: str) -> Optional[List[NewsItem]]:
        """
        Process a single website and extract relevant news items
        
        Args:
            url: Website URL to process
            
        Returns:
            List of processed NewsItem objects or None if processing fails
        """
        print(f"Processing website: {url}")
        
        try:
            # Initialize crawler
            crawler = AsyncWebCrawler(config=self.browser_config)
            await crawler.start()
            
            try:
                # Crawl the website
                result = await crawler.arun(
                    url=url,
                    config=self.crawl_config
                )
                
                if result.success:
                    # Save raw content
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    domain = urlparse(url).netloc
                    raw_filename = f"{domain}_{timestamp}.md"
                    raw_filepath = os.path.join(self.raw_dir, raw_filename)
                    
                    with open(raw_filepath, 'w', encoding='utf-8') as f:
                        f.write(result.markdown_v2.raw_markdown)
                    print(f"Saved raw content to: {raw_filepath}")
                    
                    # Parse and validate extracted content
                    try:
                        # Parse LLM output
                        parsed_items = self.parse_llm_output(result.extracted_content)
                        
                        if not parsed_items:
                            print("No valid items found in LLM output")
                            return None
                        
                        # Validate each item
                        news_items = []
                        for item in parsed_items:
                            try:
                                validated_item = NewsItem.model_validate(item)
                                news_items.append(validated_item)
                            except Exception as e:
                                print(f"Error validating item: {str(e)}")
                                continue
                        
                        if news_items:
                            # Save processed items
                            processed_filename = f"{domain}_{timestamp}_processed.json"
                            processed_filepath = os.path.join(self.processed_dir, processed_filename)
                            
                            with open(processed_filepath, 'w', encoding='utf-8') as f:
                                json.dump([item.model_dump() for item in news_items], f, indent=2)
                            
                            print(f"Saved processed items to: {processed_filepath}")
                            return news_items
                        else:
                            print("No valid news items found to process.")
                            return None
                            
                    except Exception as e:
                        print(f"Error processing content: {str(e)}")
                        return None
                else:
                    print(f"Failed to crawl {url}: {result.error_message}")
                    return None
                    
            finally:
                await crawler.close()
                
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            return None

async def main():
    # List of news websites to crawl
    websites = [
        "https://thepienews.com/",
        # Add more websites as needed
    ]
    
    print("\n=== Starting news crawling process ===")
    processor = NewsProcessor()
    print(f"Raw content will be saved to: {processor.raw_dir}")
    print(f"Processed summaries will be saved to: {processor.processed_dir}")
    
    # Process each website
    for website in websites:
        news_items = await processor.process_website(website)
        if news_items:
            print(f"\nProcessed {len(news_items)} relevant news items from {website}")
            for item in news_items:
                print(f"\nTitle: {item.title}")
                print(f"Category: {item.category}")
                print(f"Summary: {item.summary}")
                print(f"URL: {item.source_url}")
                print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())