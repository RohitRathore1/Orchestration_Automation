from pydantic import BaseModel, Field

class ItemID(BaseModel):
    """Schema for item ID input validation."""
    item_id: str = Field(..., description="The UUID of the item to fetch")

class Item(BaseModel):
    """Schema for an item, including its ID and value."""
    id: str = Field(..., description="The unique identifier for the item as a string")
    value: str = Field(..., description="The value of the item")

class ItemCreate(BaseModel):
    """Schema for creating a new item. Assumes value is a string."""
    value: str = Field(..., description="The value of the item to create")
