from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["data"]
collection = db["user"]

collection.insert_one({"name": "anshul", "email": "anshulxyz@gmail.com", "status": "active"})

for doc in collection.find():
    print(doc)
