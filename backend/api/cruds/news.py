from pymongo import MongoClient
import pymongo
import asyncio
#mongoDBのやつ
#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)

async def connect_db():
    #connect to mongodb
    DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
    client = MongoClient(DATABASE_URL)
    return await asyncio.sleep(1)

"""
db = client["test"]
my_collection = db["data"]

data_1 = {
     "Name":"test1",
     "Age":25,
 }
my_collection.insert_one(data_1)
"""
def db_create_title(title):
    print("タイトル挿入する")
    db = client["titles"]
    my_collection=db["titles"]
    result = my_collection.find_one({"Atitle":title})
    data={
        "Atitle":title
    }
    if result is None:
        my_collection.insert_one(data)
    else:
        pass

async def db_serch_title(title):
    print("タイトル確認する")
    #"title"DBがあるか確認，なければ作成
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
    

def db_create_news(news):
    print("news追加するやで")
    db = client["news"]
    my_collection=db["data"]
    title = news.get("title")
    keywords = news.get("keywords")
    content = news.get("content")
    data={
        "title":f"{title}",
        "keywords":f"{keywords}",
        "content":f"{content}"
    }
    my_collection.insert_one(data)