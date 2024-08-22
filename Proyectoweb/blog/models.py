from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)  # se utiliza para filtrar por fecha de creacion 
    updated = models.DateTimeField(auto_now_add=True)  # se utiliza para filtrar por fecha de actualizacion 

    class Meta:
        verbose_name = 'categoria'  # Esta opción define el nombre descriptivo singular que se utilizará para mostrar una instancia individual de tu modelo en el panel de administración. En este caso, se establece como "categoria".
        verbose_name_plural = 'categorias'  # Esta opción define el nombre descriptivo plural que se utilizará para mostrar múltiples instancias de tu modelo en el panel de administración. En este caso, se establece como "categorias".

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)  # agregamos estos parametros para que dentro de la carpeta media se cree una subcarpeta para la aplicacion blog y lo especificamos como opcional
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # establecemos que cuando el Autor de un post se elimina, tambien lo hagan todos sus post
    categorias = models.ManyToManyField(Categoria)  # Establecemos que cada post puede pertenecer a varias categorias y que cada categoria puede estar en varios post
    created = models.DateTimeField(auto_now_add=True)  # se utiliza para filtrar por fecha de creacion 
    updated = models.DateTimeField(auto_now_add=True)  # se utiliza para filtrar por fecha de actualizacion 

    class Meta:
        verbose_name = 'post'  # Esta opción define el nombre descriptivo singular que se utilizará para mostrar una instancia individual de tu modelo en el panel de administración. En este caso, se establece como "post".
        verbose_name_plural = 'posts'  # Esta opción define el nombre descriptivo plural que se utilizará para mostrar múltiples instancias de tu modelo en el panel de administración. En este caso, se establece como "posts".

    def __str__(self):
        return self.titulo