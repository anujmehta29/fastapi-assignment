from pydantic import BaseModel
from datetime import datetime
from pymongo.collection import Collection
from ..database import db  # Ensure this correctly imports your database connection
from bson import ObjectId

# Define the item collection
item_collection: Collection = db['items']


class ItemModel(BaseModel):
    _id: str  # Ensure this field is present
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = None  # Optional field

class Config:
        json_encoders = {
            ObjectId: str
        }

def insert_item(item_data: dict):
    # Generate a new ObjectId for the item
    item_data['_id'] = ObjectId()
    item_data['insert_date'] = datetime.utcnow()  # Use UTC for consistency

    # Insert the item into the MongoDB collection
    item_collection.insert_one(item_data)

    # Convert ObjectId to string before returning
    item_data['_id'] = str(item_data['_id'])
    print(f"Inserted Item: {item_data}")  # Debugging print
    return item_data  # Return the inserted item with the new _id


def find_item(item_id: str):
    if not ObjectId.is_valid(item_id):
        return None

    item = item_collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item['_id'] = str(item.pop('_id'))  # Convert ObjectId to str
        return item  # Return as a dictionary, not ItemModel
    return None
   

def find_all_items():
    items = list(item_collection.find())
    for item in items:
        item['_id'] = str(item['_id'])  # Convert ObjectId to str
    return [ItemModel(**item) for item in items]  # Return a list of ItemModel instances

def update_item(item_id: str, update_data: dict):
    if not ObjectId.is_valid(item_id):
        return None

    result = item_collection.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    if result.modified_count > 0:
        return find_item(item_id)  # Return the updated item
    return None  # Item not found

def delete_item(item_id: str):
    if not ObjectId.is_valid(item_id):
        return False

    result = item_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0  # Return True if item was deleted
