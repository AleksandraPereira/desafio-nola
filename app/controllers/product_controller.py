from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, ProductOut
from app.services.product_service import create_product, get_products
from app.database import SessionLocal

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductOut)
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, data)

@router.get("/", response_model=list[ProductOut])
def list_all(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    return get_products(db, skip=skip, limit=limit)
