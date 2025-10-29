from fastapi import APIRouter
from app.schemas.store_schema import StoreCreate, StoreOut
from app.services.store_service import create_store

router = APIRouter(prefix="/stores", tags=["Stores"])

@router.post("/", response_model=StoreOut)
def create(store: StoreCreate):
    return create_store(store)
