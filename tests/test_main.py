import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main_redirect():
    """Test if the root redirects to /docs"""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

def test_get_records_unauthorized():
    """Test that missing x-user-id header returns 422 (Validation Error)"""
    response = client.get("/records/")
    assert response.status_code == 422

def test_admin_can_create_record():
    """Test if Admin (ID 1) can successfully create a record"""
    payload = {
        "amount": 100.0,
        "type": "income",
        "category": "Test",
        "description": "Pytest Record"
    }
    # Passing the Admin ID in the header
    response = client.post("/records/", json=payload, headers={"x-user-id": "1"})
    assert response.status_code == 200
    assert response.json()["category"] == "Test"

def test_viewer_cannot_access_dashboard():
    """Test RBAC: Viewer (ID 3) should be forbidden from dashboard"""
    response = client.get("/dashboard/summary", headers={"x-user-id": "3"})
    assert response.status_code == 403
    assert response.json()["detail"] == "Insufficient permissions"