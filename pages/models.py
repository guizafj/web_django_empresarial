from django.db import models
from ckeditor.fields import RichTextField # se importa el richtext para el contenido
# Create your models here.
class Page(models.Model):    
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido") # se usa la instancia de richtext para el contenido
    order = models.SmallIntegerField(verbose_name="Orden", default=0) # instancia para el orden de las paginas
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']

    def __str__(self): 
        return self.title