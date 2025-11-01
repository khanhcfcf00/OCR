from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["bill_scanner"]

users_collection = db["users"]
bills_collection = db["bills"]