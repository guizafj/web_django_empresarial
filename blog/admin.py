"""
Configuración del panel de administración para la aplicación Blog.

Este módulo registra los modelos Category y Post en el sitio de administración de Django,
proporcionando opciones personalizadas de visualización, búsqueda y filtrado para facilitar
la gestión de contenidos.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Category en el admin de Django.

    Atributos:
        readonly_fields (tuple): Campos de solo lectura ('created', 'updated').
        list_display (tuple): Campos que se muestran en la lista de categorías.
        search_fields (tuple): Campos por los que se puede buscar.
        ordering (tuple): Orden de las categorías en la vista de lista.
    """
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    ordering = ('-created',)


class PostAdmin(admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Post en el admin de Django.

    Atributos:
        readonly_fields (tuple): Campos de solo lectura ('published', 'created', 'updated').
        list_display (tuple): Campos que se muestran en la lista de posts.
        search_fields (tuple): Campos por los que se puede buscar.
        list_filter (tuple): Campos por los que se puede filtrar.
        ordering (tuple): Orden de los posts en la vista de lista.
        date_hierarchy (str): Campo para navegación jerárquica por fecha.
    """
    readonly_fields = ('published', 'created', 'updated')
    list_display = ('title', 'published', 'autor', 'post_categories')
    search_fields = ('title', 'content')
    list_filter = ('categories__name', 'autor__username')
    ordering = ('-autor', 'published')
    date_hierarchy = 'published'

    def post_categories(self, obj):
        """
        Devuelve una cadena con los nombres de las categorías asociadas al post, separadas por coma.

        Args:
            obj (Post): Instancia del modelo Post.

        Returns:
            str: Nombres de las categorías separadas por coma.
        """
        return ", ".join([category.name for category in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías'


# Registro de los modelos en el panel de administración con sus configuraciones personalizadas
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)