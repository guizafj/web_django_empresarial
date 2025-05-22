"""
Configuración de la aplicación Core.

Este módulo define la configuración principal de la aplicación Core,
especificando el nombre de la app y el tipo de campo automático por defecto
para las claves primarias en los modelos.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Configuración principal para la aplicación 'core'.

    Atributos:
        default_auto_field (str): Tipo de campo automático por defecto para las claves primarias.
        name (str): Nombre de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
