from pymongo import MongoClient

#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

#connect to mongodb
DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)
print("Connected to MongoDB")


db = client["news"]#newsというDBに接続している
my_collection = db["data"]#DB:newsの中にある"data"というテーブルを見ている

data_1 = {
    "Name":"test1",
    "Age":25,
}
#my_collection.insert_one(data_1)

def db_create_news(news):

    
    pass

def db_get_news(news_id):
    #DB:newsのTABLE:dataから指定された行(news_id)をdic型で取得
    secNews = my_collection.find().limit(1)[news_id]

    #dic型を渡す
    return secNews

def db_get_newsCount():
    #DB:newsのTABLE:dataの中にある行の数を数える
    newsCount = my_collection.count_documents({})

    return newsCount
    