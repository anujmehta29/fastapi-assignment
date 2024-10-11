from fastapi import APIRouter, HTTPException
from bson import ObjectId
from ..models.item import (
    insert_item,
    find_item,
    find_all_items,
    update_item as update_item_model,
    delete_item as delete_item_from_db,  # Renamed the imported delete_item function
    ItemModel,
)

# Define the router here
router = APIRouter()

@router.post("/items", response_model=ItemModel)
async def create_item(item_data: ItemModel):
    try:
        item_dict = item_data.dict(exclude_unset=True)  # Convert the ItemModel to a dictionary
        created_item_dict = insert_item(item_dict)  # Insert item and retrieve the created item

        if created_item_dict is None:
            raise HTTPException(status_code=500, detail="Item could not be created.")

        # Create an ItemModel instance including the _id field
        created_item = ItemModel(**created_item_dict)  
        print(f"Directly returning created item: {created_item}")  # Debugging print
        return created_item  # Return the ItemModel instance
    except Exception as e:
        print(f"Error creating item: {e}")  # Debugging print
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/items", response_model=list[ItemModel])  
async def read_all_items():
    try:
        items = find_all_items()  # Retrieve all items
        return [ItemModel(**item) for item in items]  # Ensure all items conform to ItemModel
    except Exception as e:
        print(f"Error retrieving items: {e}")  # Debugging print
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/items/{item_id}", response_model=ItemModel)  
async def read_item(item_id: str):
    if not ObjectId.is_valid(item_id):  # Validate ObjectId
        raise HTTPException(status_code=400, detail="Invalid item ID format")
    
    item = find_item(item_id)  # Find the item by ID
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemModel(**item)  # Ensure the returned item conforms to ItemModel

@router.put("/items/{item_id}", response_model=ItemModel)  
async def update_item(item_id: str, item_data: ItemModel):
    if not ObjectId.is_valid(item_id):  # Validate ObjectId
        raise HTTPException(status_code=400, detail="Invalid item ID format")
    
    updated_item = update_item_model(item_id, item_data.dict(exclude_unset=True))  # Update the item
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return ItemModel(**updated_item)  # Ensure the returned item conforms to ItemModel

@router.delete("/items/{item_id}")  
async def delete_item(item_id: str):
    if not ObjectId.is_valid(item_id):  # Validate ObjectId
        raise HTTPException(status_code=400, detail="Invalid item ID format")
    
    # Check if the item exists before attempting to delete
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Attempt to delete the item
    result = delete_item_from_db(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")  # Not found in the database
    
    return {"detail": "Item deleted"}
