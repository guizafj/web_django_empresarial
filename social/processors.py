"""
Procesadores de contexto para la aplicación Social.

Este módulo define funciones que permiten agregar información adicional al contexto
de las plantillas de Django, facilitando el acceso a los enlaces de redes sociales
desde cualquier plantilla del proyecto.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from .models import Link

def ctx_dict(request):
    """
    Procesador de contexto que agrega los enlaces de redes sociales al contexto global.

    Recorre todos los objetos Link y los agrega al contexto usando como clave el 'key'
    y como valor la 'url', permitiendo acceder a cada enlace desde cualquier plantilla.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        dict: Diccionario con los enlaces de redes sociales, donde la clave es el 'key'
              y el valor es la 'url' correspondiente.
    """
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx