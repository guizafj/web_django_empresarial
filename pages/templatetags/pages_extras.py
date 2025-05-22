"""
Etiquetas personalizadas para plantillas de la aplicación Pages.

Este módulo define etiquetas de plantilla adicionales para la aplicación Pages,
permitiendo obtener listas de páginas publicadas y facilitar su uso en los templates.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django import template
from pages.models import Page

# Se registra la biblioteca de etiquetas personalizadas para plantillas
register = template.Library()

@register.simple_tag
def get_page_list():
    """
    Obtiene una lista de todas las páginas publicadas.

    Returns:
        QuerySet: Lista de instancias del modelo Page.
    """
    pages = Page.objects.all()  # Obtiene todas las páginas
    return pages  # Devuelve la lista de páginas