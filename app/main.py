from fastapi import FastAPI
from app.controllers.store_controller import router as store_controller_router
from app.controllers.customer_controller import router as customer_router
from app.controllers.product_controller import router as product_router
from app.controllers.order_controller import router as order_router
from app.controllers.analytics_controller import router as analytics_router
from app.database import Base, engine

app = FastAPI(title="Desafio Nola API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API do Desafio Nola está rodando!"}

app.include_router(store_controller_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(analytics_router)
