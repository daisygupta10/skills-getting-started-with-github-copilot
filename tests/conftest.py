import pytest
from fastapi.testclient import TestClient
from src.app import app
import copy

@pytest.fixture
def client():
    # Arrange: create a fresh TestClient and reset activities for each test
    test_client = TestClient(app)
    # Optionally, reset in-memory activities here if needed
    yield test_client
