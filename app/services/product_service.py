from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate

def create_product(db: Session, data: ProductCreate):
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product_by_id(db: Session, product_id: int, data: ProductCreate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    for key, value in data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True