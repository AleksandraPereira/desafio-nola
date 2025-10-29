from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.customer_schema import CustomerCreate, CustomerOut
from app.services.customer_service import create_customer, get_customers
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
