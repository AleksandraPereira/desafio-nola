from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.customer_schema import CustomerCreate, CustomerOut
from app.services.customer_service import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer_by_id,
    delete_customer_by_id
)
from app.database import SessionLocal

router = APIRouter(prefix="/customers", tags=["Customers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CustomerOut)
def create(data: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, data)

@router.get("/", response_model=list[CustomerOut])
def list_all(db: Session = Depends(get_db)):
    return get_customers(db)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_by_id(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return customer

@router.put("/{customer_id}", response_model=CustomerOut)
def update(customer_id: int, data: CustomerCreate, db: Session = Depends(get_db)):
    updated = update_customer_by_id(db, customer_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return updated

@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    success = delete_customer_by_id(db, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"detail": "Cliente deletado com sucesso"}