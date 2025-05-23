from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Datos de usuario
    user_data = {
        "email": "test2@example.com",
        "password": "password123"
    }

    # Registro
    response = client.post("/register", json=user_data)
    assert response.status_code == 200 or response.status_code == 201

    # Login
    response = client.post("/login", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"