from tkinter import Widget
from django import forms

# desde este modulo es posible agregar valores html a los formularios
class ContactForm(forms.Form): 
    name = forms.CharField(label='Nombre', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}), min_length=4)
    email = forms.EmailField(label='Correo electrónico', required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}), min_length=4, max_length=100)
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 2}))

    