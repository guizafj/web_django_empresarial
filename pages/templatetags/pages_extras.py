from atexit import register
from django import template
from pages.models import Page

register = template.Library()  # Se registra la biblioteca de plantillas

@register.simple_tag
def get_page_list():
    """
    Obtiene una lista de todas las páginas publicadas.
    """
    pages = Page.objects.all()  # Obtiene todas las páginas
    return pages  # Devuelve la lista de páginas