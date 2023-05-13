from pymongo import MongoClient

#mongoDBのやつ
#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

#connect to mongodb
DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)

"""
db = client["test"]
my_collection = db["data"]

data_1 = {
     "Name":"test1",
     "Age":25,
 }
my_collection.insert_one(data_1)
"""
def db_create_time(time):
    print("時間挿入するやで")
    db = client["time"]
    my_collection=db["time"]

    data={
        "date":time
    }
    my_collection.insert_one(data)
    my_collection.create_index([("date", pymongo.ASCENDING)], unique=True)

def db_serch_time(time):
    print("時間確認するで")
    db = client["time"]
    my_collection=db["time"]
    result = my_collection.find_one({"date":time})
    if result:
        return result
    else:
        return None
    

def db_create_news(news):
    print("news追加するやで")
    db = client["news"]
    my_collection=db["data"]
    data=news
    my_collection.insert_one(data)