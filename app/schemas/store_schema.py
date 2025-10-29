from pydantic import BaseModel

class StoreCreate(BaseModel):
    name: str
    brand: str

class StoreOut(StoreCreate):
    id: int

    class Config:
        from_attributes = True  # Corrigido: indentado corretamente dentro da classe
