from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class OrderItemOut(OrderItemCreate):
    id: int

    class Config:
        from_attributes = True
