from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from .models import Desarrollo

def home(request):
    desarrollos = Desarrollo.objects.all()

    # Formulario de contacto
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data['nombre']
            apellido = formulario_contacto.cleaned_data['apellido']
            telefono = formulario_contacto.cleaned_data['telefono']
            email = formulario_contacto.cleaned_data['email']
            consulta = formulario_contacto.cleaned_data['consulta']

            # Enviar email
            email_message = EmailMessage(
                "Mensaje desde App Django",
                f"Nombre: {nombre} {apellido}\nTeléfono: {telefono}\nEmail: {email}\nConsulta: {consulta}",
                "leo_91_166@hotmail.com",  # Tu dirección de correo (debe coincidir con EMAIL_HOST_USER)
                ["leo_91_166@hotmail.com"],  # Dirección a la que llega el correo
                reply_to=[email]
            )

            try:
                email_message.send()
                return redirect("/?valido")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect("/?novalido")

    return render(request, 'realestateapp/home.html', {'desarrollos': desarrollos, 'miformulario': formulario_contacto})

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            # Procesar el formulario
            # Redirigir a la misma sección de contacto
            return redirect('/#contacto')
    else:
        form = FormularioContacto()

    return render(request, 'tu_template.html', {'form': form})

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacto.html', {'miformulario': form, 'mensaje_enviado': True})
    else:
        form = FormularioContacto()
    
    return render(request, 'contacto.html', {'miformulario': form, 'mensaje_enviado': False})