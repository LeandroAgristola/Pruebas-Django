from django.shortcuts import render
from servicios.models import Servicio #importamos el servicio del models de la APP servicios para poder trabajar sobre la vista servicios

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()# le deciamos a django que importe todos los servicios que creamos 
    return render(request,"servicios/servicios.html",{"servicios":servicios})
