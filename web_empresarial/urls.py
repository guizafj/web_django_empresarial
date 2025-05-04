"""
URL configuration for web_empresarial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # se importan las configuraciones creadas para que funcionen las modificaciones realizadas



urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),  # se incluye la url de los servicios
    path('blog/', include('blog.urls')),  # se incluye la url del blog
    path('page/', include('pages.urls')),
     path('contact/', include('contact.urls')),

    # paths del admin
    path('admin/', admin.site.urls),
]


# se crea la coondición para que se puedan ver las imágenes en el navegador solo en modo de desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # aqui se accede a las imágenes por medio de las instancias creadas en settings.py