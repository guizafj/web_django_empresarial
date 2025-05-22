"""
Modelos para la aplicación Pages.

Este módulo define el modelo principal para la gestión de páginas estáticas dentro del proyecto,
permitiendo almacenar información como el título, contenido, orden y fechas de creación/actualización.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.db import models
from ckeditor.fields import RichTextField  # Se importa RichTextField para el contenido enriquecido

class Page(models.Model):
    """
    Modelo que representa una página estática del sitio.

    Atributos:
        title (str): Título de la página.
        content (RichTextField): Contenido enriquecido de la página.
        order (int): Orden de aparición de la página en listados o menús.
        created (datetime): Fecha de creación de la página.
        updated (datetime): Fecha de última actualización de la página.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")  # Campo para contenido enriquecido
    order = models.SmallIntegerField(verbose_name="Orden", default=0)  # Orden de la página
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que será el título de la página.
        """
        return self.title