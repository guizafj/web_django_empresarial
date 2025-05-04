from django.db import models
from django.utils.timezone import now # timezone es una libreria de django que permite trabajar con fechas y horas
from django.contrib.auth.models import User # se accede a todos los usuarios creados 
from ckeditor.fields import RichTextField # se importa el richtextfield para poder usar el editor de texto enriquecido
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self): 
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now) # se toma la fecha y hora actual
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor') # se crea una relación con el modelo de usuario / usando el on_delete se le indica que si se elimina el usuario, se eliminan los post creados por el
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts') # se crea una relación de muchos a muchos con la categoría
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title