from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models import User
from schemas import TokenData
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRTE_MINUTES

# Configuracion de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Esta línea crea un contexto de hashing que define cómo se van a generar y verificar los hashes de contraseñas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # Los usuarios se autentican enviando usuario y contraseña a /login, y ahí obtienen un token JWT que se usará después

# Función para obtener el hash de una contraseña
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Verificar si la contraseña ingresada coincide con el hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Crear token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRTE_MINUTES))
    to_encode.update({"exp": expire}) # Agrega expire al dict
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decodificar el token y obtener usuario
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "No se pudo validar el token",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user