from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, ProductOut
from app.services.product_service import (
    create_product,
    get_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id
)
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

@router.get("/{product_id}", response_model=ProductOut)
def get_by_id(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

@router.put("/{product_id}", response_model=ProductOut)
def update(product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    updated = update_product_by_id(db, product_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    success = delete_product_by_id(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}
