from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):

    carro=Carro(request) #agregamos el carro apenas inicia el sitio para evitar errores

    return render(request,"ProyectowebApp/home.html")
