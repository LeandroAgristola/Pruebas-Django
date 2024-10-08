from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from .models import Desarrollo

def home(request):
    desarrollos = Desarrollo.objects.all()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            # Simula la lógica del envío de correo (no se envía realmente)
            try:
                # Normalmente enviarías un correo aquí
                # email_message.send()
                # Simulación de envío exitoso:
                return JsonResponse({'status': 'ok'}, status=200)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        else:
            # Devolver errores de validación
            errores = formulario_contacto.errors.as_json()
            return JsonResponse({'status': 'invalid', 'errors': errores}, status=400)

    formulario_contacto = FormularioContacto()
    return render(request, 'realestateapp/home.html', {
        'desarrollos': desarrollos,
        'miformulario': formulario_contacto
    })

def mobileViviendas(request):
    return render(request, 'realestateapp/mobileViviendas.html')

def mobileEdificios(request):
    return render(request, 'realestateapp/mobileEdificios.html')

def mobileIndustrias(request):
    return render(request, 'realestateapp/mobileIndustrias.html')
