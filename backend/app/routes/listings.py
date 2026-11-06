from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Listing
from ..schemas import ListingCreate, ListingResponse

router = APIRouter()


@router.post("/listings/bulk")
def bulk_insert_listings(items: List[ListingCreate], db: Session = Depends(get_db)):
    if not items:
        raise HTTPException(status_code=400, detail="Please send at least one listing.")

    rows = [Listing(**item.model_dump()) for item in items]
    db.add_all(rows)
    db.commit()
    return {"message": "Listings inserted successfully", "inserted_count": len(rows)}


@router.get("/listings", response_model=List[ListingResponse])
def get_listings(
    search: Optional[str] = Query(default=None),
    skip: int = 0,
    limit: int = Query(default=20, ge=1, le=200),
    db: Session = Depends(get_db)
):
    query = db.query(Listing)
    if search:
        text = f"%{search}%"
        query = query.filter(
            (Listing.business_name.ilike(text)) |
            (Listing.category.ilike(text)) |
            (Listing.city.ilike(text))
        )
    return query.order_by(Listing.id.desc()).offset(skip).limit(limit).all()


@router.get("/dashboard/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    total = db.query(func.count(Listing.id)).scalar() or 0
    cities = db.query(func.count(func.distinct(Listing.city))).scalar() or 0
    categories = db.query(func.count(func.distinct(Listing.category))).scalar() or 0
    sources = db.query(func.count(func.distinct(Listing.source))).scalar() or 0
    return {
        "total_listings": total,
        "total_cities": cities,
        "total_categories": categories,
        "total_sources": sources
    }


def get_grouped_counts(db: Session, column):
    rows = (
        db.query(column.label("name"), func.count(Listing.id).label("count"))
        .group_by(column)
        .order_by(func.count(Listing.id).desc())
        .all()
    )
    return [{"name": row.name, "count": row.count} for row in rows]


@router.get("/dashboard/city-wise")
def city_wise(db: Session = Depends(get_db)):
    return get_grouped_counts(db, Listing.city)


@router.get("/dashboard/category-wise")
def category_wise(db: Session = Depends(get_db)):
    return get_grouped_counts(db, Listing.category)


@router.get("/dashboard/source-wise")
def source_wise(db: Session = Depends(get_db)):
    return get_grouped_counts(db, Listing.source)
