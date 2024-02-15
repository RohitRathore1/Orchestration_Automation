from uuid import UUID, uuid4
from fastapi import APIRouter, HTTPException, Depends, Path
from ..schemas import Item, ItemCreate 
from typing import Dict
import logging
import os

logger = logging.getLogger(__name__)
router = APIRouter()

def get_data_store() -> Dict[str, str]:
    data_store = {}
    current_dir = os.path.dirname(os.path.dirname(__file__))
    data_file_path = os.path.join(current_dir, 'data', 'example.data')
    with open(data_file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(" ", 1)
            data_store[key] = value
    logger.info(f"Number of items loaded into data store: {len(data_store)}")
    return data_store

@router.get("/item/{item_id}", response_model=Item)
async def read_item(item_id: str = Path(..., description="The UUID of the item to fetch as a string"), data_store: Dict = Depends(get_data_store)):
    logger.info(f"Fetching item with ID: {item_id}") 
    if item_id in data_store:
        # Directly use item_id as a string, matching the Item schema
        return Item(id=item_id, value=data_store[item_id])
    else:
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")

@router.post("/item/", response_model=Item)
async def create_item(item: ItemCreate, data_store: Dict = Depends(get_data_store)):
    new_item_id = str(uuid4())
    data_store[new_item_id] = item.value
    # Use the stringified UUID for the id field
    return Item(id=new_item_id, value=item.value)