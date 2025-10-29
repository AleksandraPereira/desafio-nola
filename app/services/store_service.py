from app.models.store import Store
from app.schemas.store_schema import StoreCreate
from app.database import SessionLocal

def create_store(store_data: StoreCreate):
    db = SessionLocal()
    new_store = Store(**store_data.dict())
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    db.close()
    return new_store
