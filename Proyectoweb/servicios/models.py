from django.db import models

# Create your models here.


class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios') #agregamos estos parametros para que dentro de la carpeta media se cree una subcarpeta para la aplicacion Servicios 
    created=models.DateTimeField(auto_now_add=True) #se utiliza para filtrar por fecha de creacion 
    updated=models.DateTimeField(auto_now_add=True) #se utiliza para filtrar por fecha de actualizacion 

    class Meta:
        verbose_name='servicio' # Esta opción define el nombre descriptivo singular que se utilizará para mostrar una instancia individual de tu modelo en el panel de administración. En este caso, se establece como "servicio".
        verbose_name_plural='servicios' #Esta opción define el nombre descriptivo plural que se utilizará para mostrar múltiples instancias de tu modelo en el panel de administración. En este caso, se establece como "servicios"

    def __str__(self):
        return self.titulo
