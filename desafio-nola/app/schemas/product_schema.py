from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str | None = None
    price: float
    margin: float | None = None

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True
