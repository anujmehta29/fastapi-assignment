from fastapi import APIRouter, HTTPException
from datetime import datetime
import logging
from ..schemas.clock_in import ClockInCreate, ClockInResponse  # Ensure correct import
from ..models.clock_in import (
    insert_clock_in,
    get_clock_in_by_id,
    get_all_clock_ins,
    delete_clock_in,
    update_clock_in,
)

router = APIRouter()
@router.post("/clock-in", response_model=ClockInResponse)
async def create_clock_in(clock_in: ClockInCreate):
    try:
        # Prepare the data to be inserted
        clock_in_data = clock_in.dict()
        clock_in_data["insert_date"] = datetime.utcnow()  # Add insert_date
        clock_in_id = insert_clock_in(clock_in_data)

        # Return response model
        response = ClockInResponse(
            id=clock_in_id,
            user_id=clock_in_data["user_id"],
            clock_in_time=clock_in_data["clock_in_time"],
            clock_out_time=None,
            insert_date=clock_in_data["insert_date"]
        )
        return response
    except HTTPException as http_exc:
        logging.error(f"HTTP Exception: {http_exc.detail}")
        raise http_exc  # Re-raise HTTP exceptions
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create clock-in.")


@router.get("/clock-in/{id}", response_model=ClockInResponse)
async def read_clock_in(id: str):
    try:
        clock_in_record = get_clock_in_by_id(id)
        if clock_in_record is None:
            raise HTTPException(status_code=404, detail="Clock-in record not found.")
        return clock_in_record
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to retrieve clock-in record.")

@router.get("/clock-in", response_model=list[ClockInResponse])
async def read_all_clock_ins():
    try:
        clock_in_records = get_all_clock_ins()
        return clock_in_records
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to retrieve clock-in records.")

@router.delete("/clock-in/{id}", response_model=dict)
async def delete_clock_in_by_id(id: str):
    try:
        result = delete_clock_in(id)  # Call the delete function
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Clock-in record not found.")
        
        logging.info(f"Deleted clock-in record with ID: {id}")
        return {"detail": "Clock-in record deleted successfully."}
    except HTTPException as http_exc:
        logging.error(f"HTTP Exception: {http_exc.detail}")
        raise http_exc  # Re-raise HTTP exceptions
    except Exception as e:
        logging.error(f"Error deleting clock-in record: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete clock-in record.")

@router.put("/clock-in/{id}", response_model=ClockInResponse)
async def update_clock_in_by_id(id: str, clock_in: ClockInCreate):
    try:
        clock_in_data = clock_in.dict()
        updated_record = update_clock_in(id, clock_in_data)
        if updated_record is None:
            raise HTTPException(status_code=404, detail="Clock-in record not found.")
        return updated_record
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to update clock-in record.")
