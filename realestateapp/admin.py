from django.contrib import admin
from .models import Desarrollo

class desarrolloAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'contenido', 'created', 'updated')
    search_fields = ('titulo',)

    # Asegúrate de que la imagen se muestre en el administrador
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="width: 100px; height: auto;" />'
        return 'No image'
    
    imagen_preview.allow_tags = True  # Para permitir etiquetas HTML
    imagen_preview.short_description = 'Imagen'

admin.site.register(Desarrollo, desarrolloAdmin)