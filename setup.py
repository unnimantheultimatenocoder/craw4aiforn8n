from setuptools import setup, find_packages

setup(
    name="crawl4ai",
    version="0.4.247",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "aiohttp>=3.8.1",
        "beautifulsoup4>=4.9.3",
        "python-multipart>=0.0.5",
        "pydantic>=1.8.2",
        "bs4>=0.0.1",
    ],
)