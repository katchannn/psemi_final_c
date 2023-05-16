from fastapi import APIRouter
from typing import List
import schemas.news as news_schema
from cruds import news as news_crud
from bson import ObjectId

router = APIRouter()


@router.get("/news", response_model=List[news_schema.News])
async def list_news():

    result= []

    for i in range(news_crud.db_get_newsCount()):

        #辞書型で格納されているid,title,keywords,contentを持ってくる
        secNews = news_crud.db_get_news(i)


        #idはbson.ObjectId型→string型
        newsId = secNews.get("_id")
        strNewsId = str(newsId)

        #タイトルと概要は普通に指定して取る
        newsTitle = secNews.get("title")
        newsContent = secNews.get("content")

        #キーワードは長い文字列のstring型→辞書型
        str_newsKeywords = secNews.get("keywords")
        dic_keywords = eval(str_newsKeywords)
    
        result.append(news_schema.News(
                id=strNewsId,
                title=newsTitle,
                keywords=dic_keywords,
                content=newsContent,
        ))
    
    return result


@router.get("/news/{news_id}", response_model=news_schema.News)
async def detail_news():
    return news_schema.News(
        id="1",
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )


@router.get("/test", response_model=news_schema.News)
async def test_news():
    return news_schema.News(
        id="1",
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )
