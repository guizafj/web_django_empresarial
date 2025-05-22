"""
Modelos de la aplicación Blog.

Este módulo define los modelos principales para la gestión de categorías y entradas (posts)
del blog, incluyendo relaciones, campos y configuraciones de visualización.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Modelo que representa una categoría para clasificar las entradas del blog.

    Atributos:
        name (str): Nombre de la categoría.
        created (datetime): Fecha de creación de la categoría.
        updated (datetime): Fecha de última actualización de la categoría.
    """
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que será el nombre de la categoría.
        """
        return self.name


class Post(models.Model):
    """
    Modelo que representa una entrada (post) del blog.

    Atributos:
        title (str): Título de la entrada.
        content (RichTextField): Contenido enriquecido de la entrada.
        published (datetime): Fecha y hora de publicación.
        image (ImageField): Imagen asociada a la entrada (opcional).
        autor (User): Usuario autor de la entrada.
        categories (Category): Categorías asociadas a la entrada.
        created (datetime): Fecha de creación de la entrada.
        updated (datetime): Fecha de última actualización de la entrada.
    """
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(
        verbose_name='Fecha de publicación',
        default=now
    )
    image = models.ImageField(
        upload_to='blog',
        verbose_name='Imagen',
        null=True,
        blank=True
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Autor'
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name='Categorías',
        related_name='get_posts'
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que será el título de la entrada.
        """
        return self.title