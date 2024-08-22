from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

# Define una clase para personalizar la apariencia y comportamiento de la administración del modelo CategoriaProd en el panel de administración de Django.
class CategoriaProdAdmin(admin.ModelAdmin):
    # Indica que los campos 'created' y 'updated' son solo de lectura en el panel de administración.
    readonly_fields = ("created", "updated")

# Define una clase para personalizar la apariencia y comportamiento de la administración del modelo Producto en el panel de administración de Django.
class ProductoAdmin(admin.ModelAdmin):  # Corrección en el nombre de la clase (era ProductodAdmin)
    # Indica que los campos 'created' y 'updated' son solo de lectura en el panel de administración.
    readonly_fields = ("created", "updated")

# Registra el modelo CategoriaProd en el panel de administración de Django usando la configuración de CategoriaProdAdmin.
admin.site.register(CategoriaProd, CategoriaProdAdmin)

# Registra el modelo Producto en el panel de administración de Django usando la configuración de ProductoAdmin.
admin.site.register(Producto, ProductoAdmin)