## Configuración

1. Copiar el archivo de variables de entorno:

    bash: cp .env.example .env
    PS: Copy-Item .env.example .env

2. Editar .env y completar los valores necesarios, como SECRET_KEY, base de datos, etc.


## Instalación de dependencias

1. Crear y activar un entorno virtual:

- En Linux/macOS:
    python -m venv venv
    source venv/bin/activate


- En Windows:
    python -m venv venv
    .\venv\Scripts\activate

2. Instalar los paquetes necesarios:

   pip install -r requirements.txt
