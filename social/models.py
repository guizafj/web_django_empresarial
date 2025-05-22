"""
Modelos para la aplicación Social.

Este módulo define el modelo principal para la gestión de enlaces a redes sociales,
permitiendo almacenar información relevante como el nombre clave, nombre visible,
URL y fechas de creación/actualización.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.db import models

class Link(models.Model):
    """
    Modelo que representa un enlace a una red social o recurso externo.

    Atributos:
        key (SlugField): Nombre clave único para identificar el enlace.
        name (CharField): Nombre visible de la red social o recurso.
        url (URLField): Enlace asociado (puede ser nulo o estar en blanco).
        created (DateTimeField): Fecha de creación del registro.
        updated (DateTimeField): Fecha de última actualización del registro.
    """
    key = models.SlugField(
        verbose_name="Nombre clave",
        max_length=100,
        unique=True
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Red social"
    )
    url = models.URLField(
        verbose_name="Enlace",
        max_length=200,
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización'
    )

    class Meta:
        """
        Metadatos para el modelo Link.
        """
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que será el nombre del enlace.
        """
        return self.name