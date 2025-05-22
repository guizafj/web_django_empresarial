"""
Definición de rutas (URLs) para la aplicación Core.

Este módulo contiene las rutas principales para acceder a las vistas centrales de la aplicación,
como la página de inicio, la página "Acerca de" y la tienda.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de inicio
    path('', views.home, name='home'),

    # Ruta para la página "Acerca de"
    path('about/', views.about, name='about'),

    # Ruta para la página de la tienda
    path('store/', views.store, name='store'),
]