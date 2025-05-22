"""
Definición de rutas (URLs) para la aplicación Blog.

Este módulo contiene las rutas principales para acceder a las vistas del blog,
incluyendo la página principal del blog y la visualización de entradas por categoría.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal del blog
    path('', views.blog, name='blog'),

    # Ruta para ver las entradas filtradas por categoría
    path('category/<int:category_id>/', views.category, name='category'),
]