"""
Configuración de la aplicación Blog.

Este módulo define la configuración principal de la aplicación Blog,
especificando el nombre de la app y el tipo de campo automático por defecto
para las claves primarias en los modelos.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuración principal para la aplicación 'blog'.

    Atributos:
        default_auto_field (str): Tipo de campo automático por defecto para las claves primarias.
        name (str): Nombre de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
