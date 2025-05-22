"""
Configuración ASGI para el proyecto web_empresarial.

Este archivo expone la variable 'application' a nivel de módulo, que es utilizada por los servidores ASGI
para servir la aplicación Django de manera asíncrona.

Para más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

import os
from django.core.asgi import get_asgi_application

# Establece la configuración por defecto de Django para el entorno ASGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_empresarial.settings')

# Obtiene la aplicación ASGI que será utilizada por el servidor
application = get_asgi_application()
