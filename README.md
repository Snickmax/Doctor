# Doctor
Sistema Gestor Doctor

Se necesita Sqlite3 protable para administrar la base de datos
    https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe

se creo con python^3.12.2

# Crear venv Instalando Virtualenv
1. intalar:
    pip install virtualenv
2. Crear virtualenv
    virtualenv venv
3. entrar al terminal venv
    .\venv\Scripts\activate
4. instalar dependencias de pip
    pip install -r requirements.txt

# Comandos Django
1. migrate DB
    python manage.py makemigrations
    python manage.py migrate
2. crear usuario
    python manage.py createsuperuser
3. correr proyecto
    python manage.py runserver

ahora puede gestionar pacientes y citas, generar reportes por dias