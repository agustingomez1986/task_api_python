from sqlalchemy import create_engine # crear una conexión al motor de base de datos
from sqlalchemy.orm import sessionmaker, declarative_base

# sessionmaker: crea una fábrica de sesiones para interactuar con la base de datos.
# declarative_base: crea una clase base a partir de la cual definirás tus modelos de tabla

# Dirección URL a la base
DATABASE_URL = "sqlite:///./app/tasks.db"

# Creo una conexión que se puede usar con varios hilos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Fabrica de sesiones (instancias)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de modelos (tablas) de la db
Base = declarative_base()

# Obtener DB (para dependencias)
def get_db():
    db = SessionLocal() # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db # FastAPI detecta funciones con yield como dependencias que necesitan limpieza
    finally:
        db.close()
