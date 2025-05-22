"""
Definición de rutas (URLs) para la aplicación Contact.

Este módulo contiene las rutas principales para acceder a las vistas de contacto,
permitiendo mostrar y gestionar el formulario de contacto.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal de contacto
    path('', views.contact, name='contact'),
]