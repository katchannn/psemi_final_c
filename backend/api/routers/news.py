from fastapi import APIRouter
from typing import List
import schemas.news as news_schema

router = APIRouter()


@router.get("/news", response_model=List[news_schema.News])
async def list_news():
    return [
        news_schema.News(
            id=1,
            title="title1",
            keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
            content="content1",
        ),
        news_schema.News(
            id=2,
            title="title2",
            keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
            content="content2",
        ),
        news_schema.News(
            id=3,
            title="title3",
            keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
            content="content3",
        ),
    ]


@router.get("/news/{news_id}", response_model=news_schema.News)
async def detail_news():
    return news_schema.News(
        id=1,
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )


@router.get("/test", response_model=news_schema.News)
async def test_news():
    return news_schema.News(
        id=1,
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )
