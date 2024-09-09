from django.contrib import admin
from .models import Desarrollo

# Register your models here.

class desarrolloAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #especificamos que nos aparezcan estos dos campos cuando agregamos un nuevos servicio

admin.site.register(Desarrollo, desarrolloAdmin) #registramos las dos clase
