"""
Vistas para la aplicación Services.

Este módulo contiene la vista principal para mostrar la lista de servicios ofrecidos por la empresa,
obteniendo los datos desde el modelo Service y renderizando la plantilla correspondiente.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.shortcuts import render
from .models import Service  # Se importa el modelo Service para utilizarlo en la vista

def services(request):
    """
    Vista para mostrar la página principal de servicios.

    Obtiene todos los servicios almacenados en la base de datos y los envía al template
    'services/services.html' mediante un diccionario de contexto.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con la lista de servicios.
    """
    services = Service.objects.all()  # Obtiene todos los servicios de la base de datos
    return render(request, 'services/services.html', {"services": services})  # Envía los servicios al template