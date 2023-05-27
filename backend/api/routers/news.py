from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
import schemas.news as news_schema
from cruds import news as news_crud


router = APIRouter()

@router.get("/news", response_model=List[news_schema.News])
async def list_news():
    res = await news_crud.db_get_newsList()
    return res


@router.get("/news/{news_id}", response_model=news_schema.News)
async def detail_news(news_id: str):
    res = await news_crud.db_get_news(news_id)
    if res:
        return res
    raise HTTPException(status_code=404, detail="News not found")

