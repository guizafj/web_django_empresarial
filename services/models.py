"""
Modelos para la aplicación Services.

Este módulo define el modelo principal para la gestión de servicios ofrecidos por la empresa,
permitiendo almacenar información relevante como título, subtítulo, contenido, imagen y fechas.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.db import models

class Service(models.Model):
    """
    Modelo que representa un servicio ofrecido por la empresa.

    Atributos:
        title (str): Título del servicio.
        subtitle (str): Subtítulo o descripción corta del servicio.
        content (str): Descripción detallada del servicio.
        image (ImageField): Imagen representativa del servicio.
        created (datetime): Fecha de creación del registro.
        updated (datetime): Fecha de última actualización del registro.
    """
    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )
    subtitle = models.CharField(
        max_length=200,
        verbose_name='Subtítulo'
    )
    content = models.TextField(
        verbose_name='Contenido'
    )
    image = models.ImageField(
        upload_to='services',
        verbose_name='Imagen'
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
        Metadatos para el modelo Service.
        """
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']  # Ordena por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        """
        Devuelve la representación en cadena del modelo, que será el título del servicio.
        """
        return self.title
