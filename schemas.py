from pydantic import BaseModel, EmailStr
from typing import Optional

# Creo esquemas de Pydantic para validar entradas y salidas, asegurar tipos y convertir automaticamente ORM en dict JSON serializables
class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool
    model_config = {
        "form_attributes": True # permite convertir un objeto SQLAlchemy en un dict automáticamente. Es clave para FastAPI cuando retornás objetos del ORM.
    }

class TaskUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    model_config = {
        "form_attributes": True # permite convertir un objeto SQLAlchemy en un dict automáticamente. Es clave para FastAPI cuando retornás objetos del ORM.
    }

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#class TokenData(BaseModel):
#    id: Optional[int] = None