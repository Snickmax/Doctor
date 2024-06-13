# Doctor

# Crear venv Instalando Virtualenv
1. intalar:
    pip install virtualenv
2. Crear virtualenv
    virtualenv venv
3. entrar al terminal venv
    .\venv\Scripts\activate

# pip requeriments
1. Si instalaste una dependencia que se utiliza actualizar requeriments
    pip freeze > requirements.txt
2. instalar dependencias de pip
    pip install -r requirements.txt

# Comandos Django

1. crear proyecto
    django-admin startproject Doctor .
2. correr proyecto
    python manage.py runserver