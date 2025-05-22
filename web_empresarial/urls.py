"""
Configuración de rutas (URLs) principal para el proyecto web_empresarial.

Este archivo define las rutas globales del proyecto, incluyendo la integración de las URLs
de las aplicaciones internas (core, services, blog, pages, contact) y la configuración
para servir archivos multimedia en modo desarrollo. Además, personaliza los títulos del panel de administración.

Autor: Francisco J Diaz G
Fecha: 2025-05-17

Notas:
- En producción, asegúrate de servir archivos estáticos y multimedia correctamente usando un servidor web.
- Personaliza los títulos del admin para mejorar la experiencia de administración.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Importa la configuración global del proyecto

urlpatterns = [
    # Ruta para la página principal (core)
    path('', include('core.urls')),

    # Ruta para la sección de servicios
    path('services/', include('services.urls')),  # Incluye las URLs de la app Services

    # Ruta para el blog
    path('blog/', include('blog.urls')),  # Incluye las URLs de la app Blog

    # Ruta para páginas estáticas
    path('page/', include('pages.urls')),  # Incluye las URLs de la app Pages

    # Ruta para el formulario de contacto
    path('contact/', include('contact.urls')),  # Incluye las URLs de la app Contact

    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
]

# Configuración para servir archivos multimedia solo en modo desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    # Permite acceder a archivos multimedia subidos por usuarios desde el navegador
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# Personalización de los títulos del panel de administración de Django
admin.site.site_header = 'La Caffetiera'
admin.site.index_title = 'Administración de La Caffetiera'
admin.site.site_title = 'La Caffetiera'
