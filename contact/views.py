from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):    
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid(): 
            name = request.POST.get("name", '')
            email = request.POST.get("email", '')
            content = request.POST.get("content", '')
           
            email = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto", 
                "de {} <{}> \n\n escribió:\n\n{}".format(name, email, content),
                "no-responder@inbox.mailtrap.io",  # Cambia a un remitente válido
                ["info@ecolibri.art"],
                reply_to=[email],
            )
            try: 
                email.send()
                # Esto se ejecuta si todo a funcionado correctamente
                return redirect(reverse('contact') + "?ok")
            except Exception as e:
                # Si ocurre un error al enviar el correo se mostrar un error
                print(f"Error al enviar el correo: {e}")  # Depuración
                return redirect(reverse('contact') + "?fail")
        else:
            print(contact_form.errors)  # Depuración
            
           
       
    return render(request, "contact/contact.html", {"form": contact_form})