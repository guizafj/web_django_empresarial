from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated') # Campos que solo se pueden leer en el admin

admin.site.register(Service, ServiceAdmin) # Registra el modelo Project en el admin