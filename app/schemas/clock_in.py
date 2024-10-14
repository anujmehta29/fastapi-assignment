# app/schemas/clock_in.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ClockInCreate(BaseModel):
    user_id: str
    clock_in_time: datetime

class ClockInResponse(BaseModel):
    id: str  # The ID of the clock-in record
    user_id: str  # The user ID (or any other identifier)
    clock_in_time: datetime  # The time the user clocked in
    clock_out_time: Optional[datetime] = None  # Optional clock-out time
    insert_date: datetime  # Timestamp of when the record was inserted
