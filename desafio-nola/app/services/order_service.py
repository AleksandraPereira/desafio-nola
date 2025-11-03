from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order_schema import OrderCreate

def create_order(db: Session, data: OrderCreate):
    order_data = data.model_dump(exclude={"items"})
    order = Order(**order_data)
    db.add(order)
    db.commit()
    db.refresh(order)


    for item_data in data.items:
        item_dict = item_data.model_dump()
        item = OrderItem(order_id=order.id, **item_dict)
        db.add(item)

    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session):
    return db.query(Order).all()
