from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_delete_task():

    # Login usuario 1
    user_data = {
        "email": "test@example.com",
        "password": "password123"
    }

    response = client.post("/login", json=user_data)
    #print("Login1 - BODY: ", response.content)
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

    response = client.post("/login", json=user_data2)
    #print("Login1 - BODY: ", response.content)
    assert response.status_code == 200
    data2 = response.json()
    assert "access_token" in data2
    assert data2["token_type"] == "bearer"
    token2 = data2["access_token"]
    headers2 = {"Authorization": f"Bearer {token2}"}

    # Usuario 2 actualiza tarea id: 2
    task2 = {
        "id": 2,
        "title": "Tarea 2 actualizada",
        "description": "Descripcion tarea 2 actualizada"
    }
    response = client.put("/tasks", json=task2, headers=headers2)
    #print("Actualizacion de tarea 4 - BODY: ", response.content)
    assert response.status_code == 200
    
    # Usuario 2 intento actualizar tarea id: 3 (perteneciente a usuario 1)
    task3 = {
        "id": 3,
        "title": "Tarea 3 actualizada",
    }
    response = client.put("/tasks", json=task3, headers=headers2)
    #print("Actualizacion de tarea 1 - BODY: ", response.content)
    assert response.status_code == 404

    # Usuario 1 elimina tarea id: 3
    response = client.delete("/tasks", params={"task_id": 4}, headers=headers)
    #print("Elimino tarea id 8 - BODY: ", response.content)
    assert response.status_code == 200
