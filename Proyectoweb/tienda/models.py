from django.db import models

# Define tus modelos aquí.

# Define un modelo que representa una categoría de productos.
class CategoriaProd(models.Model):
    # Campo de texto para almacenar el nombre de la categoría, con un máximo de 50 caracteres.
    nombre = models.CharField(max_length=50)
    # Campo de fecha y hora que se establece automáticamente cuando se crea el objeto.
    created = models.DateTimeField(auto_now_add=True)
    # Campo de fecha y hora que se establece automáticamente cuando se crea el objeto.
    updated = models.DateTimeField(auto_now_add=True)

    # Configuración de metadatos del modelo.
    class Meta:
        # Nombre amigable en singular para el modelo en el panel de administración.
        verbose_name = "CategoriaProb"
        # Nombre amigable en plural para el modelo en el panel de administración.
        verbose_name_plural = "CategoriasProb"

    # Método que define cómo se representará el objeto como una cadena de texto.
    def __str__(self):
        # Devuelve el nombre de la categoría.
        return self.nombre

# Define un modelo que representa un producto.
class Producto(models.Model):
    # Campo de texto para almacenar el nombre del producto, con un máximo de 50 caracteres.
    nombre = models.CharField(max_length=50)
    # Campo de fecha y hora que se establece automáticamente cuando se crea el objeto.
    created = models.DateTimeField(auto_now_add=True)
    # Campo de fecha y hora que se establece automáticamente cuando se crea el objeto.
    updated = models.DateTimeField(auto_now_add=True)
    # Relación de clave foránea con el modelo CategoriaProd. Si se elimina la categoría, también se elimina el producto.
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    # Campo para almacenar una imagen del producto. Se guarda en el directorio "tienda".
    imagen = models.ImageField(upload_to="tienda", null=False, blank=False)
    # Campo para almacenar el precio del producto como un número de punto flotante.
    Precio = models.FloatField()
    # Campo booleano que indica si el producto está disponible. Por defecto, está disponible (True).
    disponibilidad = models.BooleanField(default=True)

    # Configuración de metadatos del modelo.
    class Meta:
        # Nombre amigable en singular para el modelo en el panel de administración.
        verbose_name = "Producto"
        # Nombre amigable en plural para el modelo en el panel de administración.
        verbose_name_plural = "Productos"

    # Método que define cómo se representará el objeto como una cadena de texto.
    def __str__(self):
        # Devuelve el nombre del producto.
        return self.nombre
