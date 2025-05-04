from django.shortcuts import render, get_object_or_404
from .models import Post, Category # se importa el modelo creado para poder usarlo en la vista

# Create your views here.
def blog(request):
    posts = Post.objects.all() # Obtiene todos los proyectos de la base de datos
    
    return render(request, 'blog/blog.html', {"posts": posts}) # se envia con un diccionario de contexto

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id) # se obtiene la categoria por el id
    # posts = Post.objects.filter(categories=category) # se filtran los proyectos por la categoria - este es el método rudimentario
    return render(request, 'blog/category.html', {"category": category}) # se envia la categoria al template