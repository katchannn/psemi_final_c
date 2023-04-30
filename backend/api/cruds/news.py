from pymongo import MongoClient

#env
HOST = 'mongo'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'

#connect to mongodb
DATABASE_URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'
client = MongoClient(DATABASE_URL)
db = client["test"]
print("Connected to MongoDB")

my_collection = db["data"]

data_1 = {
    "Name":"test1",
    "Age":25,
}


def db_create_news(news):
    my_collection.insert_one(news)