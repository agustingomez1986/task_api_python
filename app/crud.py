from sqlalchemy.orm import Session
from app.models import User, Task
from app.schemas import UserCreate, TaskCreate, UserUpdate, TaskUpdate
from app.auth import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_pw) # Creo instancia User
    db.add(db_user) # Preparo db_user para ser enviado
    db.commit() # Hago INSERT en la base de datos
    db.refresh(db_user) # Actualizo db_user para que me traiga atributos como id
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first() # .filter() = WHERE

def delete_user_by_email(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True # Se eliminó correctamente
    return False # Error al eliminar

def update_user(user_id: int, db: Session, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    if user_update.email:
        db_user.email = user_update.email
    if user_update.password:
        db_user.hashed_password = get_password_hash(user_update.password)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(title=task.title, description=task.description, owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user.tasks
    return []

def get_task_by_owner_id(db: Session, user_id: int):
    return db.query(Task).filter(Task.owner_id == user_id).all()

def delete_task_by_id(db: Session, task_id: int, user_id: int):
    db_task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True # Se eliminó correctamente
    return False # Error al eliminar

def update_task(db: Session, task_update: TaskUpdate, user_id: int):
    db_task = db.query(Task).filter(Task.id == task_update.id, Task.owner_id == user_id).first()
    if not db_task:
        return None
    if task_update.title:
        db_task.title = task_update.title
    if task_update.description:
        db_task.description = task_update.description
    if task_update.completed is not None:
        db_task.completed = task_update.completed
    db.commit()
    db.refresh(db_task)
    return db_task
