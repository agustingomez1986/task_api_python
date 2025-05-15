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