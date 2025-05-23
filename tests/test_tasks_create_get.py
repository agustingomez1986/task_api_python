from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_get_task():

    # Login usuario 1
    user_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    response = client.post("/login", json=user_data)
    #print("Login - BODY: ", response.content)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Login usuario 2
    user_data2 = {
        "email": "test2@example.com",
        "password": "password123"
    }

    response2 = client.post("/login", json=user_data2)
    #print("Login - BODY: ", response.content)
    assert response2.status_code == 200
    data2 = response2.json()
    assert "access_token" in data2
    assert data2["token_type"] == "bearer"
    token2 = data2["access_token"]
    headers2 = {"Authorization": f"Bearer {token2}"}


    # Creo tarea usuario 1
    task1 = {
        "title": "Tarea 1",
        "description": "Descripcion tarea 1"
    }
    response = client.post("/tasks", json=task1, headers=headers)
    #print("Creación de tarea 1 - BODY1: ", response.content)
    assert response2.status_code == 200
    
    task2 = {
        "title": "Tarea 2",
        "description": "Descripcion tarea 2"
    }
    response = client.post("/tasks", json=task2, headers=headers)
    #print("Creación de tarea 1 - BODY2: ", response.content)
    assert response.status_code == 200

    # Creo tarea usuario 2
    task1_2 = {
        "title": "Tarea 1_2",
        "description": "Descripcion tarea 1_2"
    }
    response2 = client.post("/tasks", json=task1_2, headers=headers2)
    #print("Creación de tarea 1 - BODY1: ", response.content)
    assert response2.status_code == 200
    
    task2_2 = {
        "title": "Tarea 2_2",
        "description": "Descripcion tarea 2_2"
    }
    response2 = client.post("/tasks", json=task2_2, headers=headers2)
    #print("Creación de tarea 1 - BODY2: ", response.content)
    assert response2.status_code == 200

    # Obtener tarea owner_id = 2
    response = client.get("/tasks", headers=headers2)
    print("Obtener tarea - BODY: ", response.content)
    assert response.status_code == 200