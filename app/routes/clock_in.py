from fastapi import APIRouter, HTTPException
from ..schemas.clock_in import ClockInCreate, ClockInResponse
from ..models.clock_in import insert_clock_in
from datetime import datetime

router = APIRouter()

@router.post("/clock-in", response_model=ClockInResponse)
async def create_clock_in(clock_in: ClockInCreate):
    try:
        # Prepare the data to be inserted
        clock_in_data = clock_in.dict()
        clock_in_data["insert_date"] = datetime.utcnow()  # Add insert_date

        # Call the insert function
        clock_in_id = insert_clock_in(clock_in_data)

        return {"id": clock_in_id, "insert_date": datetime.utcnow()}  # Include insert_date in response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
