"""
Vistas para la aplicación Blog.

Este módulo contiene las vistas principales para mostrar las entradas del blog y
las entradas filtradas por categoría.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request):
    """
    Vista para mostrar la página principal del blog.

    Obtiene todas las entradas (posts) de la base de datos y las envía al template
    'blog/blog.html' a través del contexto.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con la lista de posts.
    """
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})


def category(request, category_id):
    """
    Vista para mostrar las entradas filtradas por una categoría específica.

    Obtiene la categoría correspondiente al 'category_id' proporcionado y la envía
    al template 'blog/category.html' a través del contexto.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.
        category_id (int): ID de la categoría a mostrar.

    Returns:
        HttpResponse: Respuesta renderizada con la información de la categoría.
    """
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {"category": category})