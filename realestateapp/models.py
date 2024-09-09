from django.db import models

# Create your models here.

class Desarrollo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='desarrollos')  # Se guardará en la carpeta media/desarrollos
    brochurePaper = models.FileField(upload_to='desarrollos_pdfs/')
    created = models.DateTimeField(auto_now_add=True)  # Se establece cuando el registro se crea por primera vez
    updated = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente cada vez que se modifica el registro

    class Meta:
        verbose_name = 'desarrollo'  # Nombre singular para el admin
        verbose_name_plural = 'desarrollos'  # Nombre plural para el admin

    def __str__(self):
        return self.titulo
