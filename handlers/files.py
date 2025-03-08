from pymongo import MongoClient
from config import MONGO_URI, HD_CONTENT_DB, DESI_CONTENT_DB

client = MongoClient(MONGO_URI)
hd_db = client[HD_CONTENT_DB]  # Database for HD content
desi_db = client[DESI_CONTENT_DB]  # Database for DESI content

def add_file(channel_id, file_id, file_type, category):
    """Adds a file to the database."""
    collection = hd_db.files if category == "HD" else desi_db.files
    collection.insert_one({"channel_id": channel_id, "file_id": file_id, "file_type": file_type})
    return True

def get_random_file(category):
    """Fetches a random file from the selected database."""
    collection = hd_db.files if category == "HD" else desi_db.files
    file = collection.aggregate([{"$sample": {"size": 1}}])
    return next(file, None)

def count_files():
    """Counts the number of files in each database."""
    return {
        "HD_CONTENT": hd_db.files.count_documents({}),
        "DESI_CONTENT": desi_db.files.count_documents({})
    }

def delete_old_files(days=5):
    """Deletes files older than a specified number of days (auto-delete feature)."""
    from datetime import datetime, timedelta
    expire_date = datetime.utcnow() - timedelta(days=days)
    hd_db.files.delete_many({"date_added": {"$lt": expire_date}})
    desi_db.files.delete_many({"date_added": {"$lt": expire_date}})
