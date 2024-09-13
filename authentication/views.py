from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroFormulario  # Importar el nuevo formulario

# Create your views here.

class VRegistro(View):
    def get(self, request):
        form = RegistroFormulario()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        form = RegistroFormulario(request.POST)  # Usar el nuevo formulario
        if form.is_valid():
            usuario = form.save()  # Guardar el usuario y la información adicional
            login(request, usuario)
            return redirect('home')  # Redireccionar al home
        else:
            for msj in form.errors.values():  # Mostrar errores de formulario
                messages.error(request, msj)
            return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request): #creamos la funcion para cerrar sesion
    logout(request)
    return redirect('home') #una vez cerrada la sesion, redireccionamos al home

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')  # Redirige al home si el login es exitoso
            else:
                messages.error(request, "Usuario no válido!")
        else:
            messages.error(request, "Información incorrecta")
    else:
        form = AuthenticationForm()

    return render(request, "login/login.html", {"form": form})