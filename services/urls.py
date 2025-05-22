"""
Definición de rutas (URLs) para la aplicación Services.

Este módulo contiene las rutas principales para acceder a las vistas de servicios,
permitiendo mostrar la página principal de servicios ofrecidos por la empresa.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal de servicios
    path('', views.services, name='services'),
]