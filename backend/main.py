from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello! Backend fastapi is working."}