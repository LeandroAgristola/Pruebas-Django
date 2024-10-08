from django.contrib import admin
from .models import Desarrollo

# Clase ModelAdmin personalizada
class desarrolloAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Campos que no se pueden editar
    # Puedes agregar más configuraciones si es necesario
    list_display = ('titulo', 'contenido', 'created', 'updated')  # Campos a mostrar en la lista
    search_fields = ('titulo',)  # Campos para buscar

admin.site.register(Desarrollo, desarrolloAdmin)  # Registro del modelo