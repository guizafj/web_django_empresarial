"""
Configuración del panel de administración para la aplicación Services.

Este módulo permite registrar y personalizar la visualización del modelo Service
en el panel de administración de Django, facilitando su gestión a través de la interfaz web.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Service en el admin de Django.

    Atributos:
        readonly_fields (tuple): Campos de solo lectura ('created', 'updated').
    """
    readonly_fields = ('created', 'updated')  # Campos que solo se pueden leer en el admin

# Registro del modelo Service con su configuración personalizada en el admin
admin.site.register(Service, ServiceAdmin)