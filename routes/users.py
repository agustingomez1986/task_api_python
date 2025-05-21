from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas import UserCreate, User, UserUpdate, UserLogin
from crud import create_user, get_user_by_email, delete_user_by_email, update_user as update_user_crud
from auth import verify_password, create_access_token, get_current_user
from database import get_db


router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email) # get_user_by_email deuelve un User
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.delete("/users")
def delete_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_user = delete_user_by_email(db, current_user.email)
    if deleted_user:
        return JSONResponse(status_code=200, content={"detail":"Usuario eliminado correctamente"})
    return JSONResponse(status_code=404, content={"detail":"Error al eliminar usuario"})
    
@router.put("/users")
def update_user(user: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if user.id != current_user.id:
        JSONResponse(status_code=404, content={"detail":"No puede actualizar otro usuario"})
    updated_user = update_user_crud(db, user)
    if updated_user:
        return JSONResponse(status_code=200, content={"detail":"Usuario actualizado"})
    return JSONResponse(status_code=404, content={"detail":"Error al actualizar usuario"})

@router.get("/users")
def get_user(user_email: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if user_email == current_user.email:
        return get_user_by_email(db, user_email)
    return JSONResponse(status_code=404, content={"detail":"No puede traer datos de otro usuario"})