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
    return redirect('Home') #una vez cerrada la sesion, redireccionamos al home

def logear(request): #creamos la funcion para iniciar sesion
    if request.method=="POST": #si el usuario apreto en el boton de Login
        form=AuthenticationForm(request,data=request.POST)#guardamos en la variable form, los datos del formulario ingresado en login
        if form.is_valid(): #si los datos del formulario login son correctos
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra) #corroboramos si los datos son correctos segun la base de dato
            if usuario is not None: # Si el usuario existe, no logea y nos redirecciona al home
                login(request, usuario)
                return redirect('Home')
            else: #si el usuario no existe
                messages.error(request,"Usuario no valido!")
        else: #la informacion no se a introducido correctamente
            messages.error(request,"Informacion incorrecta")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})