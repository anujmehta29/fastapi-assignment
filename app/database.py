# app/database.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URL from environment variable
MONGODB_URI = os.getenv('MONGODB_URI')  # Update to use MONGODB_URI

# Check if MONGODB_URI is set
if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable not set.")

print(f"Connecting to MongoDB at {MONGODB_URI}")  # Debug statement

# Create a MongoDB client
client = MongoClient(MONGODB_URI)  # Use the correct connection string

# Define the database name
db = client['FastAPI-Assignment']  # Change this to your actual database name

# Define the collections
item_collection = db['items']  # Collection name for items
