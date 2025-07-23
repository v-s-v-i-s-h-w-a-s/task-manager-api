from fastapi.testclient import TestClient
from app.main import app  # <- this needs the PYTHONPATH fix

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
