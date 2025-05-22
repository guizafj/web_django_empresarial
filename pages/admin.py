"""
Configuración del panel de administración para la aplicación Pages.

Este módulo permite registrar y personalizar la visualización del modelo Page
en el panel de administración de Django, facilitando su gestión a través de la interfaz web.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Page en el admin de Django.

    Atributos:
        readonly_fields (tuple): Campos de solo lectura ('created', 'updated').
        list_display (tuple): Campos que se muestran en la lista de páginas (título y orden).
    """
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')  # Muestra el título y el orden personalizado de la página

# Registro del modelo Page con su configuración personalizada en el admin
admin.site.register(Page, PageAdmin)