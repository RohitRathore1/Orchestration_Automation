from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from fastapi.security import HTTPBasicCredentials
from fastapi import Depends
from app.dependencies import get_current_user
from app.routes.item_routes import router as item_router
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global data_store dictionary to simulate database storage
data_store = {}

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Loading data into data_store...")
    try:
        current_file_dir = os.path.dirname(__file__)  
        data_file_path = os.path.join(current_file_dir, 'data', 'example.data')
        
        with open(data_file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(" ", 1)
                data_store[key] = value
            logger.info(f"Loaded {len(lines)} items into data_store.")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")

app.include_router(item_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Key-Value Store!"}

@app.get("/debug/datastore")
async def debug_datastore():
    return data_store

@app.get("/debug/item/{item_id}")
def get_specific_item(item_id: str):
    item = data_store.get(item_id, None)
    if item:
        return {item_id: item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# You can also directly add routes here if small in number or for simplicity
@app.get("/status")
async def status(credentials: HTTPBasicCredentials = Depends(get_current_user)):
    """A simple status check endpoint, protected by basic authentication."""
    return {"status": "Application is running", "user": credentials.username}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)