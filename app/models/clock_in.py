from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime
import os

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["your_database_name"]  # Ensure this matches your setup
clock_in_collection = db["clock_in"]  # Ensure this matches your setup

def insert_clock_in(clock_in_data: dict):
    clock_in_data["insert_date"] = datetime.utcnow()  # Add current timestamp
    result = clock_in_collection.insert_one(clock_in_data)
    return str(result.inserted_id)
