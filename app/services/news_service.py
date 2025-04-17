import httpx
from app.config import NEWSAPI_KEY, BASE_URL


async def fetch_all_news(page: int = 1, page_size: int = 20):
    url = f"{BASE_URL}/everything?q=bitcoin&page={page}&pageSize={page_size}&apiKey={NEWSAPI_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()


async def fetch_top_headlines_by_country(country: str):
    url = f"{BASE_URL}/top-headlines?country={country}&apiKey={NEWSAPI_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()


async def fetch_top_headlines_by_source(source: str):
    url = f"{BASE_URL}/top-headlines?sources={source}&apiKey={NEWSAPI_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()


async def fetch_top_headlines_filtered(country: str, source: str):
    url = f"{BASE_URL}/top-headlines?country={country}&sources={source}&apiKey={NEWSAPI_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()
