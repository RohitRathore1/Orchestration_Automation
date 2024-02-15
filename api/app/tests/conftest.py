import pytest
from fastapi.testclient import TestClient
from main import app  # replace with the name of your FastAPI file

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client