from django.shortcuts import render
from .models import Desarrollo  # Asegúrate de importar tu modelo si lo necesitas

def home(request):
    desarrollos = Desarrollo.objects.all()  # Si estás usando este modelo
    return render(request, 'realestateapp/home.html', {'desarrollos': desarrollos})