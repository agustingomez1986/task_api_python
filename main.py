from fastapi import FastAPI # Importa la clase `FastAPI`, que es la base para crear tu aplicación web.
from routes import users, tasks # Se espera que cada uno contenga un router (un conjunto de rutas relacionadas).

# Crea una instancia de la aplicación FastAPI.
app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "API de gestión de tareas"}