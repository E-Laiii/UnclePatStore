from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from pydantic import BaseModel
import logging

# FastAPI app
app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#Logging Template
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# SQLite database setup
DATABASE_URL = "sqlite:///./items.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Database model
class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index= True)

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    description: str
    price: float

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Checking if fastapi is working 
@app.get("/")
async def read_root():
    return {"message": "Hello! Backend fastapi is working."}

# POST API Call to create new items in store
@app.post("/items/", response_model=Item)
async def create_item(item: Item, db: Session = Depends(get_db)):

    # Create item with all values
    db_item = ItemModel(name=item.name, description=item.description, price = item.price)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    # Log the event
    logging.info(f"Item added: {item}")

    return db_item

# GET API Call to get all items in store
@app.get("/items/", response_model=None)
def get_all_items():

    # Fetch list of items from the database
    db = SessionLocal()
    items = db.query(ItemModel).all()
    db.close()

    # Log the event
    logging.info(f"List of items fetched successfully")

    return items

# PUT API Call to update selected items within store
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):

    # Fetch item that was selected according to id
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)

    # Log the event
    logging.info(f"Item Updated: {item}")

    return item

# DELETE API Call up delete selected items within store
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int, db: Session = Depends(get_db)):

    # Fetch item that was selected according to id
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(db_item)
    db.commit()

    # Log the event
    item_name = db_item.name
    logging.info(f"Item Deleted: {item_name}")

    return db_item