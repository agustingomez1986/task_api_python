from sqlalchemy.orm import Session
from models import User, Task
from schemas import UserCreate, TaskCreate
from auth import get_password_hash

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
        return True
    return False

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

def get_task_by_owner_id(db: Session, user_id: str):
    return db.query(Task).filter(Task.owner_id == user_id).all()