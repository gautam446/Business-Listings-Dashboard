from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base


class Listing(Base):
    __tablename__ = "listing_master"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String(255), nullable=False)
    category = Column(String(120), nullable=False)
    city = Column(String(120), nullable=False)
    address = Column(Text, nullable=True)
    phone = Column(String(30), nullable=True)
    source = Column(String(120), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
