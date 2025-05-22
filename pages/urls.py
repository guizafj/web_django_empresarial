"""
Definición de rutas (URLs) para la aplicación Pages.

Este módulo contiene las rutas principales para acceder a las vistas de páginas estáticas,
permitiendo mostrar el detalle de una página específica a través de su ID y slug.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para mostrar el detalle de una página estática según su ID y slug
    path('<int:page_id>/<slug:page_slug>', views.page, name='page'),
]