from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    store_id = Column(Integer, nullable=False)
    channel = Column(String, nullable=False)
    status = Column(String, nullable=False)
    total_value = Column(Float, nullable=False)
    discount = Column(Float, nullable=True)
    created_at = Column(DateTime)
    prep_time = Column(Integer, nullable=True)
    delivery_time = Column(Integer, nullable=True)

    customer = relationship("Customer", backref="orders")
    items = relationship("OrderItem", back_populates="order")
