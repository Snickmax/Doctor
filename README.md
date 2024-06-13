# Doctor
Se necesita Sqlite3 protable
    https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe

se creo con python^3.12.2

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
    django-admin startproject nameproyect .
2. correr proyecto
    python manage.py runserver
2. crear app
    python manage.py startapp nameapp
3. migrate DB
    python manage.py makemigrations
    python manage.py migrate
4. crear usuario
    python manage.py createsuperuser