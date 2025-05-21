from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskCreate, User, TaskUpdate
from auth import get_current_user
from database import get_db
from sqlalchemy.orm import Session
from crud import create_task, delete_task_by_id, update_task as update_task_crud, get_task_by_owner_id
from models import Task as TaskModel

router = APIRouter()

@router.post("/tasks")
def register_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task, current_user.id)

@router.delete("/tasks")
def delete_task(task_id: int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    deleted_task = delete_task_by_id(db, task_id, current_user.id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no pertenece al usuario")
    return True

@router.put("/tasks")
def update_task(task_update: TaskUpdate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_task = update_task_crud(db, task_update, current_user.id)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada o no pertenece al usuario")
    return True

@router.get("/tasks")
def get_task(db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    gotten_task = get_task_by_owner_id(db, current_user.id)
    if gotten_task:
        return gotten_task
    return []