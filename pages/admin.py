from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order') # Se muestra el titulo y el orden usando la insntancia de order para personalizar el orden

admin.site.register(Page, PageAdmin)