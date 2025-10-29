from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerCreate

def create_customer(db: Session, data: CustomerCreate):
    customer = Customer(**data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_customers(db: Session):
    return db.query(Customer).all()
