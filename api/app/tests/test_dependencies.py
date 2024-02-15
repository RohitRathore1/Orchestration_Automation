# tests/conftest.py
import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from app.main import app 

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as test_client:
        yield test_client