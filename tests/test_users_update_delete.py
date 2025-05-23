from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_delete():
    user_data = {
        "email": "test9@example.com",
        "password": "nuevopassword"
    }

    user_update_email = {
        "email": "nuevomail@test.com"
    }

    user_update_password = {
        "password": "nuevopassword"
    }

    # Login
    response = client.post("/login", json=user_data)
    #print("Actualización de email: Login: BODY", response.content)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    #response = client.put("/users", json=user_update_password, headers=headers)
    #print("Actualización de email: Update: BODY", response.content)
    #assert response.status_code == 200

    response = client.delete("/users", headers = headers)
    assert response.status_code == 200