import csv
from app.database import SessionLocal
from app.models.store import Store

db = SessionLocal()

with open('../stores.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print("Linha lida:", row)

        store = Store(
            name=row['name'],
            brand=row['brand_id']
        )
        db.add(store)

db.commit()
db.close()