from django.contrib import admin
from .models import Servicio

# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #especificamos que nos aparezcan estos dos campos cuando agregamos un nuevos servicio

admin.site.register(Servicio, servicioAdmin) #registramos las dos clases 