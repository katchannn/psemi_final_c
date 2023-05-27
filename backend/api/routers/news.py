from fastapi import APIRouter
from typing import List
import schemas.news as news_schema
from cruds import db_get_newslist


router = APIRouter()


@router.get("/news", response_model=List[news_schema.News])
async def list_news():
    return db_get_newslist()

   
  

@router.get("/news/{news_id}", response_model=news_schema.News)

async def detail_news(news_id:str):

    secNews = {}#詳細を表示したいニュースの辞書型

    #ここで該当するニュースをみつける
    for i in range(news_crud.db_get_newsCount()):

        findNews = news_crud.db_get_news(i)#テーブルから行をひとつ出す

        searchNewsId = findNews.get("_id")
        str_searchNewsId = str(searchNewsId)#その中のidを抽出(bson.object→string型)

        if(news_id == str_searchNewsId):#検索
            secNews = findNews#この部分で結果を辞書型を格納
            break

            


    #idはbson.ObjectId型→string型
    newsId = secNews.get("_id")
    strNewsId = str(newsId)

    #タイトルと概要は普通に指定して取る
    newsTitle = secNews.get("title")
    newsContent = secNews.get("content")

    #キーワードは長い文字列のstring型→辞書型
    str_newsKeywords = secNews.get("keywords")
    dic_keywords = eval(str_newsKeywords)
    
    #imgsrc,htmlsrcはどちらも文字列(?)
    newsImgSrc = secNews.get("img")
    newsHtmlSrc = secNews.get("html")

    

    return news_schema.News(
        id=strNewsId,
        html=newsHtmlSrc,
        img=newsImgSrc,
        title=newsTitle,
        keywords=dic_keywords,
        content=newsContent,
    )


@router.get("/test", response_model=news_schema.News)
async def test_news():
    return news_schema.News(
        id="1",
        html="htmlsrc1",
        img="img1",
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )
