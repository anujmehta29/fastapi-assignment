from pydantic import BaseModel
from datetime import datetime

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInResponse(BaseModel):
    id: str
    insert_date: datetime
