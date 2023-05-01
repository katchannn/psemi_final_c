from fastapi import APIRouter
from typing import List
import schemas.news as news_schema

router = APIRouter()

@router.get("/news")
async def list_news():
    pass

@router.get("/news/{news_id}")
async def detail_news():
    pass

@router.get("/news/test", response_model=List[news_schema.News])
async def test_news():
    return [news_schema.News(id=1, title="Test", description="Test")]