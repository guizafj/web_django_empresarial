"""
Vistas para la aplicación Core.

Este módulo contiene las vistas principales de la aplicación Core, incluyendo la página de inicio,
la página "Acerca de" y la tienda. Cada vista se encarga de renderizar la plantilla correspondiente.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.shortcuts import render, HttpResponse

def home(request):
    """
    Vista para la página de inicio.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla de inicio.
    """
    return render(request, "core/index.html")

def about(request):
    """
    Vista para la página "Acerca de".

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla "about".
    """
    return render(request, "core/about.html")

def store(request):
    """
    Vista para la página de la tienda.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con la plantilla de la tienda.
    """
    return render(request, "core/store.html")




