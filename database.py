from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI


client = AsyncIOMotorClient(MONGO_URI)

db = client["bio_mute_bot"]

users_collection = db["users"]
groups_collection = db["groups"]
warnings_collection = db["warnings"]
approved_collection = db["approved_users"]
sudo_collection = db["sudo_users"]
stats_collection = db["stats"]