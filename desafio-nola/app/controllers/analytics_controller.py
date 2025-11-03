from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.analytics_service import (
    get_top_products_by_day_channel,
    get_ticket_medio_por_canal_loja,
    get_low_margin_products,
    get_delivery_performance,
    get_lost_customers
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/top-products")
def top_products(day: str, channel: str, db: Session = Depends(get_db)):
    return get_top_products_by_day_channel(db, day, channel)

@router.get("/ticket-medio")
def ticket_medio(db: Session = Depends(get_db)):
    return get_ticket_medio_por_canal_loja(db)

@router.get("/low-margin-products")
def low_margin(db: Session = Depends(get_db)):
    return get_low_margin_products(db)

@router.get("/delivery-performance")
def delivery_performance(db: Session = Depends(get_db)):
    return get_delivery_performance(db)

@router.get("/lost-customers")
def lost_customers(db: Session = Depends(get_db)):
    return get_lost_customers(db)
