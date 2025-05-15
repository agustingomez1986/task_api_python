from sqlalchemy.orm import Session
from models import User, Task
from schemas import UserCreate, TaskCreate
from auth import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user