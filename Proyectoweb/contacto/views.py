from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data['nombre']
            email = formulario_contacto.cleaned_data['email']
            contenido = formulario_contacto.cleaned_data['contenido']

          # Configuración del mail que recibimos
            email_message = EmailMessage(
                "Mensaje desde App Django",  # Asunto del correo
                f"El usuario con nombre {nombre} con la dirección {email} escribe lo siguiente:\n\n{contenido}",  # Contenido del correo
                "leo_91_166@hotmail.com",  # Desde donde viene el mail (debe ser la misma que EMAIL_HOST_USER)
                ["leo_91_166@hotmail.com"],  # A qué cuenta lo gestiona
                reply_to=[email]  # Permitir responder a este mail
            )

            try:
                email_message.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")  # Imprimir el error con más detalles
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {"miformulario": formulario_contacto})