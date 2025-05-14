from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def obtener_usuarios():
    return [{"nombre": "Agustín"}, {"nombre": "Lucas"}]