# Web Django Empresarial

Web desarrollada como práctica dentro de la formación en backend con Django. Este proyecto simula una página empresarial con funcionalidades como un blog, servicios, contacto y más.

## Características
- Gestión de usuarios y autenticación.
- Blog con editor de texto enriquecido (CKEditor).
- Página de servicios empresariales.
- Formulario de contacto funcional.
- Diseño modular con aplicaciones Django.

## Requisitos Previos
- Python 3.8 o superior.
- Django 5.2.
- Entorno virtual configurado.
- Base de datos SQLite (por defecto).

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/guizafj/web_django_empresarial.git
   cd web_django_empresarial

2. Crea y activa el entorno virtual:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

3. Instala las dependencias
    ```bash
    pip install -r requirements.txt

4. Aplica las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Ejecuta el servidor
    ```bash
    python manage.py runserver

