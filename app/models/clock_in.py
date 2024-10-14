from bson import ObjectId
from pymongo import MongoClient
from datetime import datetime
import os
import logging
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["FastAPI-Assignment"]  # Ensure this matches your setup
clock_in_collection = db["clock_in"]  # Ensure this matches your setup

# ClockIn model definition
class ClockIn(BaseModel):
    user_id: str
    clock_in_time: datetime

class ClockInResponse(BaseModel):
    id: str
    user_id: str
    clock_in_time: datetime
    clock_out_time: Optional[datetime] = None  # This should already be correct
    insert_date: datetime



def insert_clock_in(clock_in_data: dict):
    try:
        clock_in_data["insert_date"] = datetime.utcnow()  # Add current timestamp
        result = clock_in_collection.insert_one(clock_in_data)
        return str(result.inserted_id)  # Return the inserted ID as a string
    except Exception as e:
        logging.error(f"Error inserting clock-in data: {e}")  # Log the exact error
        raise  # Re-raise the exception to handle it at a higher level

# Function to get all clock-in records
def get_all_clock_ins() -> List[ClockInResponse]:
    records = clock_in_collection.find()
    return [ClockInResponse(
        id=str(record["_id"]),
        user_id=record["user_id"],
        clock_in_time=record["clock_in_time"],
        clock_out_time=record.get("clock_out_time"),
        insert_date=record["insert_date"]
    ) for record in records]

# Function to get a clock-in record by ID
def get_clock_in_by_id(clock_in_id: str) -> ClockInResponse:
    record = clock_in_collection.find_one({"_id": ObjectId(clock_in_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    
    return ClockInResponse(
        id=str(record["_id"]),
        user_id=record["user_id"],
        clock_in_time=record["clock_in_time"],
        clock_out_time=record.get("clock_out_time"),
        insert_date=record["insert_date"]
    )

# Function to update a clock-in record by ID
def update_clock_in(clock_in_id: str, updated_data: dict) -> ClockInResponse:
    result = clock_in_collection.update_one(
        {"_id": ObjectId(clock_in_id)},
        {"$set": updated_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found or no update performed")
    
    return get_clock_in_by_id(clock_in_id)

# Function to delete a clock-in record by ID


def delete_clock_in(id: str):
    try:
        result = clock_in_collection.delete_one({"_id": ObjectId(id)})
        logging.info(f"Delete result for ID {id}: {result.deleted_count}")
        return result
    except Exception as e:
        logging.error(f"Error deleting clock-in with ID {id}: {e}")
        raise  # Re-raise to handle at a higher level
