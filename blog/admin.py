from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):  
    readonly_fields = ('created', 'updated') # se le indica que los campos creados y actualizados no se pueden editar
    list_display = ('name', 'created', 'updated') # se le indica que se muestren los campos nombre, fecha de creación y fecha de actualización
    search_fields = ('name',) # se le indica que se pueda buscar por el campo nombre
    ordering = ('-created',) # se le indica que se ordene por fecha de creación, de más reciente a más antiguo

class PostAdmin(admin.ModelAdmin):  
    readonly_fields = ('published', 'created', 'updated') # se le indica que los campos publicados, creados y actualizados no se pueden editar
    list_display = ('title', 'published', 'autor', 'post_categories',) # se le indica que se muestren los campos título, fecha de publicación y autor
    search_fields = ('title', 'content') # se le indica que se pueda buscar por el campo título y contenido
    # La busqueda se puede hacer por el campo título y contenido o por lo que se especifique en la tupla
    # para poder buscar por autor es necesario usar autor__username ya que es un dato relacional igual sucede con las categorías
    list_filter = ('categories__name', 'autor__username',) # se le indica que se pueda filtrar por el campo categorías    
    ordering = ('-autor', 'published') # se le indica que se ordene por fecha de creación, de más reciente a más antiguo
    date_hierarchy = 'published' # se le indica que se muestre un calendario para seleccionar la fecha de publicación

    def post_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all().order_by('name')]) # se le indica que se muestre el nombre de la categoría en lugar del id de la categoría
    post_categories.short_description = 'Categorías' # se le indica que se muestre el nombre de la categoría en lugar del id de la categoría    
admin.site.register(Category, CategoryAdmin) # se registra el modelo de categoría con la clase de administración creada
admin.site.register(Post, PostAdmin) # se registra el modelo de post con la clase de administración creada