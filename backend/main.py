from fastapi import FastAPI
import logging
from models import Item

app = FastAPI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


store = []

@app.get("/")
async def root():
    return {"message": "hello! Backend fastapi is working."}
