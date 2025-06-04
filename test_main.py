from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_booking_validation():
    response = client.post("/book", json={
        "class_id": 999,
        "client_name": "Test",
        "client_email": "test@example.com"
    })
    assert response.status_code == 404
