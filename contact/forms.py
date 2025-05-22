"""
Formularios para la aplicación Contact.

Este módulo define los formularios utilizados en la aplicación Contact,
permitiendo la validación y gestión de los datos enviados por los usuarios
a través del formulario de contacto.

Autor: Francisco J Diaz G
Fecha: 2025-05-17
"""

from django import forms

# Formulario de contacto para recibir mensajes de los usuarios
class ContactForm(forms.Form):
    """
    Formulario para el envío de mensajes de contacto.

    Campos:
        name (CharField): Nombre del remitente.
        email (EmailField): Correo electrónico del remitente.
        content (CharField): Mensaje enviado por el usuario.
    """
    name = forms.CharField(
        label='Nombre',
        max_length=100,
        min_length=4,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        })
    )
    email = forms.EmailField(
        label='Correo electrónico',
        max_length=100,
        min_length=4,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )
    content = forms.CharField(
        label='Mensaje',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Mensaje',
            'rows': 2
        })
    )

