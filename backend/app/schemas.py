from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ListingCreate(BaseModel):
    business_name: str = Field(min_length=1, max_length=255)
    category: str = Field(min_length=1, max_length=120)
    city: str = Field(min_length=1, max_length=120)
    address: Optional[str] = None
    phone: Optional[str] = None
    source: str = Field(min_length=1, max_length=120)


class ListingResponse(ListingCreate):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
