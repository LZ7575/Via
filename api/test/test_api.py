from fastapi.testclient import TestClient
from src.api import app
from httpx import Response

client = TestClient(app)

def test_read_main():
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Not Found"}

def test_api():
    response: Response = client.get("/pets")
    assert response.status_code == 200
