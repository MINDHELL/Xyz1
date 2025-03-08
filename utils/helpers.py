import random, string
from database.db import user_verifications
from config.config import SHORTENER_API, SHORTENER_URL

async def generate_verification_link(user_id):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    verify_url = f"https://t.me/{SHORTENER_URL}?start=verify-{user_id}-{token}"
    
    user_verifications.insert_one({"user_id": user_id, "token": token, "verified": False})
    return verify_url

async def check_verification(user_id):
    user = user_verifications.find_one({"user_id": user_id, "verified": True})
    return bool(user)
