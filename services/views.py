from django.shortcuts import render
from .models import Service # se importa el modelo creado para poder usarlo en la vista
# Create your views here.

def services(request):
    services = Service.objects.all() # Obtiene todos los proyectos de la base de datos
   
    return render(request, 'services/services.html', {"services": services}) # se envia con un diccionario de contexto