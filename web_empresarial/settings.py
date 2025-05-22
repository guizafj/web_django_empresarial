"""
Configuración principal de Django para el proyecto web_empresarial.

Este archivo contiene todas las configuraciones necesarias para el funcionamiento del proyecto,
incluyendo aplicaciones instaladas, bases de datos, rutas de archivos estáticos y multimedia,
configuración de plantillas, internacionalización, validación de contraseñas y ajustes de correo electrónico.

Autor: Francisco J Diaz G
Fecha: 2025-05-17

Notas:
- Mantén la clave SECRET_KEY fuera de control de versiones en producción.
- Cambia DEBUG a False en entornos productivos.
- Configura correctamente ALLOWED_HOSTS antes de desplegar.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Construye las rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Configuración de seguridad
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-!@#qwertyuiopasdfghjklzxcvbnm')
DEBUG = True  # Cambia a False en producción
ALLOWED_HOSTS = []

# Definición de aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'ckeditor',  # Editor de texto enriquecido
    'contact',
    'core',
    'pages.apps.PagesConfig',
    'services.apps.ServicesConfig',
    'social.apps.SocialConfig',
]

# Middleware del proyecto
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs principales
ROOT_URLCONF = 'web_empresarial.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],  # Ruta de las plantillas personalizadas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.processors.ctx_dict',  # Procesador de contexto para enlaces sociales
            ],
        },
    },
]

# Configuración WSGI
WSGI_APPLICATION = 'web_empresarial.wsgi.application'

# Configuración de la base de datos (por defecto, SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Ruta para archivos estáticos personalizados
]

# Archivos multimedia (subidas de usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta para archivos multimedia

# Tipo de campo automático por defecto para claves primarias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}

# Configuración de correo electrónico usando variables de entorno
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_DEFAULT_SENDER = os.getenv('EMAIL_DEFAULT_SENDER')

# Fin de la configuración
