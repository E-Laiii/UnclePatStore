from fastapi import FastAPI, HTTPException
import logging
from models import Item
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Checking if item is out of range or not
    if item_id < 0 or item_id >= len(store):
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Update the item
    store[item_id] = item

    # Log the event
    logging.info(f"Item Updated: {item}")

    return {"message": "Item updated successfully", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Checking if item is out of range or not
    if item_id < 0 or item_id >= len(store):
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Delete the item
    deleted_item = store.pop(item_id)

    # Access the name of the deleted item directly from the Item instance
    deleted_item_name = deleted_item.name

    # Log the event
    logging.info(f"Item Deleted: {deleted_item_name}")

    return {"message": "Item deleted successfully", "item": deleted_item_name}
