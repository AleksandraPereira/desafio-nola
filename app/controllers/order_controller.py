from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.order_schema import OrderCreate, OrderOut
from app.services.order_service import create_order, get_orders
from app.database import SessionLocal

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderOut)
def create(data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, data)

@router.get("/", response_model=list[OrderOut])
def list_all(db: Session = Depends(get_db)):
    return get_orders(db)
