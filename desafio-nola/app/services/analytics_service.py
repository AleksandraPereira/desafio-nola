from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.customer import Customer

def get_top_products_by_day_channel(db: Session, day: str, channel: str):
    return db.query(
        Product.name,
        func.sum(OrderItem.quantity).label("total_sold")
    ).join(OrderItem).join(Order).filter(
        func.strftime('%w', Order.created_at) == day,
        Order.channel == channel,
        Order.status == "completed"
    ).group_by(Product.name).order_by(func.sum(OrderItem.quantity).desc()).limit(5).all()

def get_ticket_medio_por_canal_loja(db: Session):
    return db.query(
        Order.channel,
        Order.store_id,
        func.avg(Order.total_value).label("ticket_medio")
    ).filter(Order.status == "completed").group_by(Order.channel, Order.store_id).all()

def get_low_margin_products(db: Session):
    return db.query(Product).filter(Product.margin < 0.1).all()

def get_delivery_performance(db: Session):
    return db.query(
        func.strftime('%w', Order.created_at).label("dia"),
        func.strftime('%H', Order.created_at).label("hora"),
        func.avg(Order.delivery_time).label("media_entrega")
    ).filter(Order.status == "completed").group_by("dia", "hora").all()

def get_lost_customers(db: Session):
    cutoff = datetime.now() - timedelta(days=30)
    return db.query(Customer).filter(
        ~Customer.orders.any(Order.created_at > cutoff),
        Customer.orders.any(func.count(Order.id) >= 3)
    ).all()
