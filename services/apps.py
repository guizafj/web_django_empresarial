from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    verbose_name = 'Gestor de Servicios'  # Nombre que se mostrará en el admin y se traduce a español
 