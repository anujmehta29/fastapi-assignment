from pydantic import BaseModel
from datetime import datetime
from pymongo.collection import Collection
from ..database import db  # Ensure this correctly imports your database connection
from bson import ObjectId
from typing import Optional, List

# Define the item collection
item_collection: Collection = db['items']

# Pydantic model for Item
class Item(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: Optional[datetime] = None  # Auto-set on insert
    id: Optional[str] = None  # MongoDB _id field as string

    class Config:
        # Allows Pydantic to serialize ObjectId as a string
        json_encoders = {ObjectId: str}

# Insert item into the database
def insert_item(item_data: dict) -> dict:
    # Generate a new ObjectId for the item
    item_data['_id'] = ObjectId()
    # Use UTC for consistency in dates
    item_data['insert_date'] = datetime.utcnow()

    # Insert the item into the MongoDB collection
    item_collection.insert_one(item_data)

    # Convert ObjectId to string before returning the inserted item
    item_data['id'] = str(item_data.pop('_id'))  # Move _id to id field
    print(f"Inserted Item: {item_data}")  # Debugging print
    return item_data  # Return the inserted item with the new id

def find_item(item_id: str):
    item = item_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item['id'] = str(item['_id'])  # Convert ObjectId to string and assign to id
        item.pop('_id')  # Optionally remove the original _id if you don't want it in the response
    return item



# Find all items in the collection
def find_all_items() -> List[Item]:
    # Find all items in the MongoDB collection
    items = list(item_collection.find())
    # Convert ObjectId to string for each item
    for item in items:
        item['id'] = str(item.pop('_id'))
    # Return a list of Item instances
    return [Item(**item) for item in items]

# Update an item by its ID
def update_item(item_id: str, update_data: dict) -> Optional[Item]:
    if not ObjectId.is_valid(item_id):
        return None

    # Update the item in MongoDB
    result = item_collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.modified_count > 0:
        return find_item(item_id)  # Return the updated item
    return None  # Item not found or no update applied

# Delete an item by its ID
def delete_item(item_id: str) -> bool:
    if not ObjectId.is_valid(item_id):
        return False

    # Delete the item from MongoDB
    result = item_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0  # Return True if the item was deleted
