from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
def obtener_tareas():
    return [{"1": "Hacer compras"}, {"2": "Cortar pasto"}]