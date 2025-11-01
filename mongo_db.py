from pymongo import MongoClient

MONGO_URI = "mongodb+srv://khanhcfcf00:MRmagical123@cluster0.o5huuaw.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())
db = client["bill_scanner"]

users_collection = db["users"]

bills_collection = db["bills"]

