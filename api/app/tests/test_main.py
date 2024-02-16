import pytest
from .conftest import client

# Test different Endpoints
@pytest.mark.asyncio
async def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Key-Value Store!"}
    
@pytest.mark.asyncio
async def test_missing_item(client):
    response = client.get("/item/nonexistent-item-id")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_read_item(client):
    # Direct call without await
    response = client.get("/item/54b54e11-cf8f-4bdd-8261-14a9472ebfeb")
    assert response.status_code == 200
    
# test data manipulation

@pytest.mark.asyncio
async def test_create_item(client):
    response = client.post("/item/", json={"key": "new-item", "value": "New item value"})
    assert response.status_code == 200  # Or 201 for Created

# Test edge cases
@pytest.mark.asyncio
async def test_create_item_invalid_data(client):
    response = client.post("/item/", json={"invalid": "data"})
    assert response.status_code == 422  # Assuming validation error returns a 422