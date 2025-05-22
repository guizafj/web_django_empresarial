"""
Configuración de la aplicación Services.

Este módulo define la configuración principal de la aplicación Services,
especificando el nombre de la app, el tipo de campo automático por defecto
para las claves primarias en los modelos y el nombre descriptivo para el admin.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.apps import AppConfig


class ServicesConfig(AppConfig):
    """
    Configuración principal para la aplicación 'services'.

    Atributos:
        default_auto_field (str): Tipo de campo automático por defecto para las claves primarias.
        name (str): Nombre interno de la aplicación.
        verbose_name (str): Nombre descriptivo para mostrar en el panel de administración.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    verbose_name = 'Gestor de Servicios'  # Nombre que se mostrará en el admin y se traduce a español
