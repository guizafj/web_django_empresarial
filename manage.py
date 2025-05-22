#!/usr/bin/env python
"""
Utilidad de línea de comandos para tareas administrativas de Django.

Este archivo permite ejecutar comandos administrativos como iniciar el servidor,
aplicar migraciones, crear superusuarios, entre otros, para el proyecto web_empresarial.

Autor: Francisco J Diaz G
Fecha: 2025-05-17

Notas:
- Asegúrate de tener el entorno virtual activado antes de ejecutar comandos.
- No modifiques este archivo salvo que sepas exactamente lo que haces.
"""

import os
import sys


def main():
    """
    Ejecuta tareas administrativas de Django.

    Establece la configuración por defecto del proyecto y ejecuta el comando recibido
    desde la línea de comandos.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_empresarial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu variable de entorno PYTHONPATH? "
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
