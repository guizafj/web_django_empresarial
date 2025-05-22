"""
Vistas para la aplicación Contact.

Este módulo contiene la vista principal para gestionar el formulario de contacto,
incluyendo la validación de datos y el envío de correos electrónicos.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contact(request):
    """
    Vista para mostrar y procesar el formulario de contacto.

    Si la petición es GET, muestra el formulario vacío.
    Si la petición es POST y el formulario es válido, envía un correo electrónico
    con los datos proporcionados y redirige mostrando un mensaje de éxito o error.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta renderizada con el formulario o redirección tras el envío.
    """
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Extrae los datos del formulario
            name = request.POST.get("name", '')
            email = request.POST.get("email", '')
            content = request.POST.get("content", '')

            # Configura el correo electrónico a enviar
            email_message = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto",
                "de {} <{}> \n\n escribió:\n\n{}".format(name, email, content),
                "no-responder@inbox.mailtrap.io",  # Cambia a un remitente válido en producción
                ["info@ecolibri.art"],
                reply_to=[email],
            )
            try:
                email_message.send()
                # Redirige con mensaje de éxito si el correo se envía correctamente
                return redirect(reverse('contact') + "?ok")
            except Exception as e:
                # Redirige con mensaje de error si ocurre una excepción al enviar el correo
                print(f"Error al enviar el correo: {e}")  # Mensaje de depuración
                return redirect(reverse('contact') + "?fail")
        else:
            # Muestra errores de validación en consola para depuración
            print(contact_form.errors)

    # Renderiza el formulario de contacto (GET o POST con errores)
    return render(request, "contact/contact.html", {"form": contact_form})