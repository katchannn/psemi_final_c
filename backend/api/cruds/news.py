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


db = client["test"]#testというDBに接続している
my_collection = db["data"]#DB:testの中にある"data"というテーブルを見ている

data_1 = {
    "Name":"test1",
    "Age":25,
}
#my_collection.insert_one(data_1)

def db_create_news(news):

    
    pass

def db_get_news(news_id):
    #DBからニュースをとってくる
    print("@@@@@@@@@@@@db_get_news Zone!!!!@@@@@@@@@@@@")
    getNews = my_collection.find().limit(1)[news_id]
    print(getNews)#{'_id': ObjectId('645b49673a376b1569de5c14'), 'Name': 'test1', 'Age': 25}という情報を取得できた。