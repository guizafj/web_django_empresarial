"""
Configuración WSGI para el proyecto web_empresarial.

Este archivo expone la variable 'application' a nivel de módulo, que es utilizada por los servidores WSGI
para servir la aplicación Django en entornos de producción o desarrollo.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

import os
from django.core.wsgi import get_wsgi_application

# Establece la configuración por defecto de Django para el entorno WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_empresarial.settings')

# Obtiene la aplicación WSGI que será utilizada por el servidor
application = get_wsgi_application()
