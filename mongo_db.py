from pymongo import MongoClient

client = MongoClient("mongodb+srv://khanhcfcf00:MRmagical123@cluster0.o5huuaw.mongodb.net/")

db = client["bill_scanner"]

users_collection = db["users"]

bills_collection = db["bills"]


