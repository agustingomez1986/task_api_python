from pydantic import BaseModel, EmailStr

# Creo esquemas de Pydantic para validar entradas y salidas, asegurar tipos y convertir automaticamente ORM en dict JSON serializables
class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True # permite convertir un objeto SQLAlchemy en un dict automáticamente. Es clave para FastAPI cuando retornás objetos del ORM.

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
