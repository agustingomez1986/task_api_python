🧠 Task API Python
==================

API RESTful para la gestión de tareas, desarrollada con FastAPI y SQLAlchemy. Incluye autenticación JWT, operaciones CRUD para usuarios y tareas, y pruebas automatizadas con Pytest.

🚀 Tecnologías utilizadas
-------------------------

- Python 3.13
- FastAPI – Framework moderno y de alto rendimiento para construir APIs.
- SQLAlchemy – ORM para la interacción con bases de datos SQLite.
- JWT (JSON Web Tokens) – Autenticación segura de usuarios.
- Pydantic – Validación de datos basada en esquemas.
- Pytest – Framework para pruebas automatizadas.

📦 Estructura del proyecto
--------------------------

task_api_python/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       ├── users.py
│	└── tasks.py
├── tests/
│   ├── __init__.py
│   ├── test_tasks_create_get.py
│   ├── test_tasks_update_delete.py
│   ├── test_users_register_and_login.py
│   └── test_users_update_delete.py
├── .env
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

🛠️ Instalación y ejecución
---------------------------

1. Clonar el repositorio:

   git clone https://github.com/agustingomez1986/task_api_python.git
   cd task_api_python

2. Crear y activar un entorno virtual:

   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Unix o MacOS:
   source venv/bin/activate

3. Instalar las dependencias:

   pip install -r requirements.txt

4. Modificar archivo con variables de entorno:

   # En Windows:
   Copy-Item .env.example .env
   # En Unix o MacOS:
   cp .env.example .env

5. Ejecutar la aplicación:

   uvicorn app.main:app --reload

   La API estará disponible en: http://localhost:8000

🔐 Autenticación y autorización
-------------------------------

- Registro de usuarios: POST /register
- Inicio de sesión: POST /login (retorna un token JWT)
- Rutas protegidas: Requieren el encabezado Authorization: Bearer <token>

📋 Endpoints principales
------------------------

- POST /register – Registro de nuevos usuarios.
- POST /login – Autenticación de usuarios existentes.
- GET /users/me – Obtener información del usuario autenticado.
- PUT /users – Actualizar información del usuario.
- DELETE /users – Eliminar la cuenta del usuario.
- POST /tasks – Crear una nueva tarea.
- GET /tasks – Listar todas las tareas del usuario.
- PUT /tasks/{task_id} – Actualizar una tarea existente.
- DELETE /tasks/{task_id} – Eliminar una tarea específica.

✅ Pruebas automatizadas
------------------------

Para ejecutar las pruebas con Pytest:

    pytest -s tests/

Asegúrate de que el entorno virtual esté activado y que las dependencias estén instaladas.