from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.order_item_schema import OrderItemCreate, OrderItemOut

class OrderCreate(BaseModel):
    customer_id: int
    store_id: int
    channel: str
    status: str
    total_value: float
    discount: float | None = None
    created_at: datetime
    prep_time: int | None = None
    delivery_time: int | None = None
    items: List[OrderItemCreate]

class OrderOut(BaseModel):
    id: int
    customer_id: int
    store_id: int
    channel: str
    status: str
    total_value: float
    discount: float | None
    created_at: datetime
    prep_time: int | None
    delivery_time: int | None
    items: List[OrderItemOut]

    class Config:
        from_attributes = True
