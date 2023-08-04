from fastapi import FastAPI
import logging
from models import Item

app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


store = []

@app.get("/")
async def root():
    return {"message": "hello! Backend fastapi is working."}

@app.post("/items/")
def add_item(item: Item):
    # Append the item to the store list
    store.append(item)

    # Log the event
    logging.info(f"Item added: {item}")

    return {"message": "Item added successfully", "item": item}

@app.get("/items/")
def get_all_items():

    # Log the event
    logging.info(f"List of items fetched successfully")

    # Fetch list of items
    return store

