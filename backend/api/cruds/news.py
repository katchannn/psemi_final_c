from pymongo import MongoClient
import pymongo
import asyncio
from bson.objectid import ObjectId

#mongoDBのやつ
#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)
db = client["news"]
my_collection=db["data"]

async def connect_db():
    #connect to mongodb
    DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
    client = MongoClient(DATABASE_URL)
    return await asyncio.sleep(1)

def db_create_title(title):
    print("タイトル挿入する")#デバッグプリント
    db = client["titles"]
    my_collection=db["titles"]
    result = my_collection.find_one({"Atitle":title})
    #Atitleは記事のタイトル,statusはnewsに登録しているか
    data={
        "Atitle":title,
        "state":"NotStored"
    }
    if result is None:
        my_collection.insert_one(data)
    else:
        pass

async def db_serch_title(title):
    print("タイトル確認する")#デバッグプリント
    #"titles"DBがあるか確認，なければ作成
    db_names = client.list_database_names()
    if "titles" not in db_names:
        db_create_title(title)
    db = client["titles"]
    my_collection=db["titles"]
    #dateがあるか確認，見つかればその値を返す，なければnone
    result = my_collection.find_one({"Atitle":title})
    print(result)
    if result is not None:
        return result
    else:
        return None
    
def db_title_update_status(title):
    db = client["titles"]
    titles_collection = db["titles"]
    titles_collection.update_one({"Atitle": title}, {"$set": {"state": "Stored"}})


def db_create_news(news,html,img_URL):
    print("news追加する")#デバッグプリント
    db = client["news"]
    my_collection=db["data"]
    title = news.get("title")
    keywords = news.get("keywords")
    content = news.get("content")
    data={
        "html":f"{html}",
        "img":f"{img_URL}",
        "title":f"{title}",
        "keywords":keywords,
        "content":f"{content}"
    }
    my_collection.insert_one(data)
    
    
def news_serializer(news) -> dict:
    return {
        "id": str(news["_id"]),
        "html": news["html"],
        "img": news["img"],
        "title": news["title"],
        "keywords": news["keywords"],
        "content": news["content"]
    } 
    

async def db_get_news(news_id) -> dict:
    news = my_collection.find_one({"_id":ObjectId(news_id)})
    news = news_serializer(news)
    
    return news

    
async def db_get_newsList() -> list:
    newsDoc = my_collection.find().sort("_id",pymongo.DESCENDING)
    newsList = [news_serializer(news) for news in newsDoc]
    
    return newsList