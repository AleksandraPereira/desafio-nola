from fastapi import APIRouter, HTTPException
from app.schemas.store_schema import StoreCreate, StoreOut
from app.services.store_service import (
    create_store,
    get_all_stores,
    get_store_by_id,
    update_store_by_id,
    delete_store_by_id
)

router = APIRouter(prefix="/stores", tags=["Stores"])

@router.post("/", response_model=StoreOut)
def create(store: StoreCreate):
    return create_store(store)

@router.get("/", response_model=list[StoreOut])
def list_stores():
    return get_all_stores()

@router.get("/{store_id}", response_model=StoreOut)
def get_store(store_id: int):
    store = get_store_by_id(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return store

@router.put("/{store_id}", response_model=StoreOut)
def update_store(store_id: int, store: StoreCreate):
    updated = update_store_by_id(store_id, store)
    if not updated:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return updated

@router.delete("/{store_id}")
def delete_store(store_id: int):
    success = delete_store_by_id(store_id)
    if not success:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return {"detail": "Loja deletada com sucesso"}