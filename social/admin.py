"""
Configuración del panel de administración para la aplicación Social.

Este módulo permite registrar y personalizar la visualización del modelo Link
en el panel de administración de Django, facilitando su gestión a través de la interfaz web.
Incluye lógica para definir campos de solo lectura según el grupo del usuario.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.contrib import admin
from django.http import HttpRequest
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Link en el admin de Django.

    - readonly_fields: Por defecto, 'created' y 'updated' son de solo lectura.
    - get_readonly_fields: Si el usuario pertenece al grupo 'Personal', los campos 'key' y 'name'
      también serán de solo lectura; en caso contrario, solo 'created' y 'updated'.
    """
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request: HttpRequest, obj=None):
        """
        Determina los campos de solo lectura según el grupo del usuario.

        Args:
            request (HttpRequest): La solicitud HTTP recibida.
            obj (Link, opcional): Instancia del modelo Link.

        Returns:
            tuple: Campos que serán de solo lectura en el admin.
        """
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

# Registro del modelo Link con su configuración personalizada en el admin
admin.site.register(Link, LinkAdmin)