from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título') # Verbose_name es el nombre que se le da al campo que se mostrara en el admin
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta: # usada para definir metadatos de la clase
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created'] # ordena por fecha de creación, de más reciente a más antiguo

    def __str__(self):
        return self.title
