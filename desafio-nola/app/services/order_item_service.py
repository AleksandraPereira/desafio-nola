from sqlalchemy.orm import Session
from app.models.order_item import OrderItem

def get_order_items(db: Session):
    return db.query(OrderItem).all()
