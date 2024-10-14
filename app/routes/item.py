from fastapi import APIRouter, HTTPException
from bson import ObjectId
from ..models.item import (
    insert_item,
    find_item,
    find_all_items,
    update_item as update_item_model,
    delete_item as delete_item_from_db,
    Item,  # The updated Item model
)

# Initialize the router
router = APIRouter()

@router.post("/items", response_model=Item)
async def create_item(item_data: Item):
    try:
        # Convert the Item Pydantic model to a dictionary
        item_dict = item_data.dict(exclude_unset=True)
        
        # Insert the item into the database
        created_item_dict = insert_item(item_dict)

        if created_item_dict is None:
            raise HTTPException(status_code=500, detail="Item could not be created.")

        # Print the created item
        print(f"Directly returning created item: {created_item_dict}")

        # Return the created item with the new ObjectId as id
        return Item(**created_item_dict)  # Use Item model for consistency
    except Exception as e:
        print(f"Error creating item: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/items", response_model=list[Item])
async def read_all_items():
    try:
        # Retrieve all items from the database
        items = find_all_items()
        return items  # Already returns a list of Item instances
    except Exception as e:
        print(f"Error retrieving items: {e}")
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):  # Keep it synchronous
    # Validate ObjectId
    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    # Find the item by its ID
    item = find_item(item_id)  # This should now return a dictionary

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Return the found item using the Item model
    return Item(**item)  # This should work if item is a dictionary

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item_data: Item):
    # Validate ObjectId
    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    # Update the item in the database
    updated_item = update_item_model(item_id, item_data.dict(exclude_unset=True))

    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Return the updated item using the Item model
    return Item(**updated_item)

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    # Validate ObjectId
    if not ObjectId.is_valid(item_id):
        raise HTTPException(status_code=400, detail="Invalid item ID format")

    # Check if the item exists before attempting deletion
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Delete the item from the database
    result = delete_item_from_db(item_id)

    if not result:
        raise HTTPException(status_code=404, detail="Item not found")

    # Return success message
    return {"detail": "Item deleted successfully"}
