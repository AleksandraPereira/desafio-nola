from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product import Product

router = APIRouter()

@router.get("/products/")
def get_products(skip: int = Query(0), limit: int = Query(10), db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()
