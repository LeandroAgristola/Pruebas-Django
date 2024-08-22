from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Obtener el modelo de usuario, ya sea personalizado o el predeterminado de Django.
User = get_user_model()

# Definición del modelo Pedido, que representa un pedido hecho por un usuario.
class Pedido(models.Model):
    # Relación de clave foránea con el modelo de usuario. Si el usuario se elimina, se elimina el pedido.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Fecha de creación del pedido, se establece automáticamente al crearse.
    created_at = models.DateField(auto_now_add=True)

    # Método mágico que devuelve una representación en cadena del pedido.
    def __str__(self):
        # Muestra el ID del pedido como su representación en cadena.
        return str(self.id)

    # Propiedad que calcula el total del pedido sumando los subtotales de cada línea de pedido.
    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    # Metadatos del modelo para especificar el nombre de la tabla y otras configuraciones.
    class Meta:
        # Nombre de la tabla en la base de datos.
        db_table = 'pedidos'
        # Nombre singular del modelo en el panel de administración.
        verbose_name = 'pedido'
        # Nombre plural del modelo en el panel de administración.
        verbose_name_plural = 'pedidos'
        # Ordenar los pedidos por su ID de manera ascendente.
        ordering = ['id']

# Definición del modelo LineaPedidos, que representa un producto en un pedido específico.
class LineaPedidos(models.Model):
    # Relación de clave foránea con el usuario. Si se elimina el usuario, se eliminan las líneas de pedidos asociadas.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relación de clave foránea con el producto. Si el producto se elimina, se elimina la línea de pedido.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # Relación de clave foránea con el pedido. Si el pedido se elimina, se eliminan las líneas de pedido asociadas.
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    # Almacena la cantidad del producto en el pedido. Por defecto, es 1.
    cantidad = models.IntegerField(default=1)
    # Fecha de creación de la línea de pedido, se establece automáticamente al crearse.
    created_at = models.DateField(auto_now_add=True)

    # Método mágico que devuelve una representación en cadena de la línea de pedido.
    def __str__(self):
        # Muestra la cantidad y el nombre del producto en esta línea de pedido.
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    # Metadatos del modelo para especificar el nombre de la tabla y otras configuraciones.
    class Meta:
        # Nombre de la tabla en la base de datos.
        db_table = 'lineapedidos'
        # Nombre singular del modelo en el panel de administración.
        verbose_name = 'lineapedido'
        # Nombre plural del modelo en el panel de administración.
        verbose_name_plural = 'lineapedidos'
        # Ordenar las líneas de pedido por su ID de manera ascendente.
        ordering = ['id']