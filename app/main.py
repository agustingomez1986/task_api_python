from fastapi import FastAPI # Importa la clase `FastAPI`, que es la base para crear tu aplicación web.
from app.routes import users, tasks # Se espera que cada uno contenga un router (un conjunto de rutas relacionadas).
from app.database import Base, engine


# Crea una instancia de la aplicación FastAPI.
app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "API de gestión de tareas"}

# Creo tablas en la DB si todavía no existen
Base.metadata.create_all(bind=engine) # engine es la conexión a la DB