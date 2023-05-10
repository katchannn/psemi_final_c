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


# db = client["test"]
# my_collection = db["data"]

# data_1 = {
#     "Name":"test1",
#     "Age":25,
# }
# my_collection.insert_one(data_1)

def db_create_news(news):
    pass

def db_get_news(news_id):
    pass