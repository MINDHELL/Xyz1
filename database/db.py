from pymongo import MongoClient
from config.config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["telegram_bot"]

premium_users = db["premium_users"]
user_verifications = db["user_verifications"]
indexed_files = db["indexed_files"]
