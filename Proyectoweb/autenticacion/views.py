from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

class VRegistro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST) #guardamos el usuario y la contraseña que el Usuario introdujo en el form de registro
        if form.is_valid(): #si el formulario es valido: 
            usuario=form.save() #guardamos la informacion introducida en la base de datos (tabla auth_user)
            login(request,usuario) #automaticamente cuando se crea el usuario, se logea
            return redirect('Home') #una vez creado el usuarios, redireccionamos al home
        else:
            for msj in form.error_messages: #recorremos cada msj de error que haya en el formulario
                messages.error(request, form.error_messages[msj])
            return render(request,"registro/registro.html",{"form":form}) #mostramos el formulario con los errores 
        

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

