from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_get_task():

    # Login
    user_data1 = {
        "email": "test2@example.com",
        "password": "password123"
    }

    response = client.post("/login", json=user_data1)
    print("Login1 - BODY: ", response.content)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    token1 = data["access_token"]
    headers1 = {"Authorization": f"Bearer {token1}"}

    # Creo tarea
    task1 = {
        "title": "Tarea 4",
        "description": "Descripcion tarea 4"
    }
    response = client.post("/tasks", json=task1, headers=headers1)
    print("Creación de tarea 1 - BODY1: ", response.content)
    assert response.status_code == 200
    
    task2 = {
        "title": "Tarea 5",
        "description": "Descripcion tarea 5"
    }
    response = client.post("/tasks", json=task2, headers=headers1)
    print("Creación de tarea 1 - BODY2: ", response.content)
    assert response.status_code == 200

    # Obtener tarea owner_id = 1
    user_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    response = client.post("/login", json=user_data)
    print("Login - BODY: ", response.content)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.get("/tasks", headers=headers)
    print("Obtener tarea - BODY: ", response.content)
    assert response.status_code == 200