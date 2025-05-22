"""
Vistas para la aplicación Pages.

Este módulo contiene la vista principal para mostrar el detalle de una página estática,
obtenida por su ID y slug, y renderiza la plantilla correspondiente.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, page_id, page_slug):
    """
    Vista para mostrar el detalle de una página estática.

    Obtiene la página correspondiente al ID proporcionado y la pasa al template
    'pages/sample.html' para su visualización.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.
        page_id (int): ID de la página a mostrar.
        page_slug (str): Slug de la página (no se usa para la consulta, pero puede usarse para SEO).

    Returns:
        HttpResponse: Respuesta renderizada con la información de la página.
    """
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page': page})