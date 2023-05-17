from fastapi import APIRouter
from typing import List
import schemas.news as news_schema
from cruds import news as news_crud


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
    


    return news_schema.News(
        id=strNewsId,
        title=newsTitle,
        keywords=dic_keywords,
        content=newsContent,
    )


@router.get("/test", response_model=news_schema.News)
async def test_news():
    return news_schema.News(
        id="1",
        title="title1",
        keywords={"key1": "value1", "key2": "value2", "key3": "value3"},
        content="content1",
    )
