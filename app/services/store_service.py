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

def get_all_stores():
    db = SessionLocal()
    stores = db.query(Store).all()
    db.close()
    return stores

def get_store_by_id(store_id: int):
    db = SessionLocal()
    store = db.query(Store).filter(Store.id == store_id).first()
    db.close()
    return store

def update_store_by_id(store_id: int, store_data: StoreCreate):
    db = SessionLocal()
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        db.close()
        return None
    for key, value in store_data.dict().items():
        setattr(store, key, value)
    db.commit()
    db.refresh(store)
    db.close()
    return store

def delete_store_by_id(store_id: int):
    db = SessionLocal()
    store = db.query(Store).filter(Store.id == store_id).first()
    if not store:
        db.close()
        return False
    db.delete(store)
    db.commit()
    db.close()
    return True