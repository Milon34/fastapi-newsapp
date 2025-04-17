from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import NewsOut
from app.services import news_service
from app.models import News
from app.auth import oauth2_scheme
from datetime import datetime
import logging

router = APIRouter(prefix="/news", tags=["news"])


@router.get("", response_model=dict)
async def get_all_news(page: int = Query(1, ge=1), page_size: int = Query(20, ge=1),
                       token: str = Depends(oauth2_scheme)):
    try:
        logging.info("Fetching all news articles.")  # demo logger
        data = await news_service.fetch_all_news(page=page, page_size=page_size)
        return data
    except Exception as e:
        logging.error(f"Error occurred while fetching news: {e}")
        raise


@router.post("/save-latest", response_model=list[NewsOut])
async def save_latest_news(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        news_data = await news_service.fetch_all_news(page=1, page_size=3)
        articles = news_data.get("articles", [])[:3]
        saved_articles = []
        for article in articles:
            existing = db.query(News).filter(News.url == article.get("url")).first()
            if existing:
                saved_articles.append(existing)
                continue
            published_at_str = article.get("publishedAt")
            published_at = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ")
            news_item = News(
                title=article.get("title"),
                description=article.get("description"),
                url=article.get("url"),
                publishedAt=published_at
            )
            db.add(news_item)
            db.commit()
            db.refresh(news_item)
            saved_articles.append(news_item)
        return saved_articles
    except Exception as e:
        logging.error(f"Error occurred while save latest news: {e}")
        raise


@router.get("/headlines/country/{country_code}")
async def get_headlines_by_country(country_code: str, token: str = Depends(oauth2_scheme)):
    try:
        data = await news_service.fetch_top_headlines_by_country(country=country_code)
        return data
    except Exception as e:
        logging.error(f"Error occurred while get headline by country: {e}")


@router.get("/headlines/source/{source_id}")
async def get_headlines_by_source(source_id: str, token: str = Depends(oauth2_scheme)):
    try:
        data = await news_service.fetch_top_headlines_by_source(source=source_id)
        return data
    except Exception as e:
        logging.error(f"Error occurred while headline by source: {e}")


@router.get("/headlines/filter")
async def get_headlines_filtered(country: str, source: str, token: str = Depends(oauth2_scheme)):
    try:
        data = await news_service.fetch_top_headlines_filtered(country=country, source=source)
        return data
    except Exception as e:
        logging.error(f"Error occurred while headline filtered by country and source news: {e}")
