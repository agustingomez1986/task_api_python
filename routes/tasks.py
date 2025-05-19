from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskCreate, User
from auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import create_task

router = APIRouter()

@router.post("/tasks")
def register_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task, current_user.id)


@router.get("/tasks")
def obtener_tareas():
    return [{"1": "Hacer compras"}, {"2": "Cortar pasto"}]