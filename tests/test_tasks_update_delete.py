from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_update_delete_task():

    # Login
    user_data1 = {
        "email": "test2@example.com",
        "password": "password123"
    }

    response = client.post("/login", json=user_data1)
    #print("Login1 - BODY: ", response.content)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    token1 = data["access_token"]
    headers1 = {"Authorization": f"Bearer {token1}"}

    # Actualizo tarea
    task1 = {
        "id": 4,
        "title": "Tarea 4 actualizada",
        "description": "Descripcion tarea 4 actualizada"
    }
    response = client.put("/tasks", json=task1, headers=headers1)
    #print("Actualizacion de tarea 4 - BODY: ", response.content)
    assert response.status_code == 200
    
    task2 = {
        "id": 1,
        "title": "Tarea 1 actualizada",
    }
    response = client.put("/tasks", json=task2, headers=headers1)
    #print("Actualizacion de tarea 1 - BODY: ", response.content)
    assert response.status_code == 404

    # Elimino tarea

    response = client.delete("/tasks", params={"task_id": 8}, headers=headers1)
    #print("Elimino tarea id 8 - BODY: ", response.content)
    assert response.status_code == 200

    response = client.delete("/tasks", params={"task_id": 2}, headers=headers1)
    #print("Elimino tarea id 2 - BODY: ", response.content)
    assert response.status_code == 404