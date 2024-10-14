from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes.item import router as item_router
from app.routes.clock_in import router as clock_in_router  # Import the clock-in router

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection Setup
client = None
database = None

@app.on_event("startup")
async def startup_event():
    global client, database
    mongodb_uri = os.getenv("MONGODB_URI")
    if mongodb_uri:
        client = AsyncIOMotorClient(mongodb_uri)  # Initialize the MongoDB client
        database = client['FastAPI-Assignment']  # Set the database name to FastAPI-Assignment
        print("MongoDB URI loaded successfully.")
    else:
        print("MongoDB URI not found. Please check your .env file.")

@app.on_event("shutdown")
async def shutdown_event():
    global client
    if client:
        client.close()  # Close the MongoDB connection on shutdown
        print("MongoDB connection closed.")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# Include routers
app.include_router(item_router, prefix="/api", tags=["items"])
app.include_router(clock_in_router, prefix="/api", tags=["clock-in"])  # Ensure the router is included

# Optionally, expose the database instance to use in your routes
def get_database():
    return database
