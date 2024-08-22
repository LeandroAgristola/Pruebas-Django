# Define una clase que representará el carro de compras.
class Carro:
    # El constructor de la clase. Se ejecuta al crear una instancia de Carro.
    def __init__(self, request):
        # Guarda la solicitud (request) proporcionada al crear el carro.
        self.request = request
        # Obtiene la sesión del usuario a partir de la solicitud.
        self.session = request.session
        # Intenta obtener el carro de la sesión. Si no existe, crea uno nuevo como un diccionario vacío.
        carro = self.session.get("carro")
        if not carro:
            # Si el carro no existe en la sesión, inicializa uno vacío.
            carro = self.session["carro"] = {}
        # Si el carro existe, lo asigna al atributo de la instancia.
        self.carro = carro

    # Método para guardar el carro en la sesión.
    def guardar_carro(self):
        # Actualiza la sesión con el contenido del carro actual.
        self.session["carro"] = self.carro
        # Marca la sesión como modificada para asegurarse de que se guarde.
        self.session.modified = True

    # Método para agregar un producto al carro.
    def agregar(self, producto):
        # Verifica si el producto no está ya en el carro usando su ID.
        if (str(producto.id) not in self.carro.keys()):
            # Si el producto no está en el carro, lo agrega con la cantidad inicial de 1.
            self.carro[producto.id] = {
                "producto_id": producto.id,          # Almacena el ID del producto.
                "nombre": producto.nombre,           # Almacena el nombre del producto.
                "precio": str(producto.Precio),      # Almacena el precio como una cadena de texto.
                "cantidad": 1,                       # Inicializa la cantidad del producto en 1.
                "imagen": producto.imagen.url        # Almacena la URL de la imagen del producto.
            }
        else:
            # Si el producto ya está en el carro, incrementa la cantidad en 1.
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    # Aumenta el precio del producto en una unidad.
                    value["precio"] = float(value["precio"]) + producto.Precio
                    break
        # Guarda los cambios en la sesión.
        self.guardar_carro()

    # Método para eliminar un producto del carro.
    def eliminar(self, producto):
        # Convierte el ID del producto a cadena de texto.
        producto.id = str(producto.id)
        # Si el producto está en el carro, lo elimina.
        if producto.id in self.carro:
            del self.carro[producto.id]
            # Guarda los cambios en la sesión.
            self.guardar_carro()

    # Método para restar cantidad de un producto en el carro.
    def restar_producto(self, producto):
        # Recorre el carro para encontrar el producto.
        for key, value in self.carro.items():
            if key == str(producto.id):
                # Disminuye la cantidad del producto en 1.
                value["cantidad"] = value["cantidad"] - 1
                # Disminuye el precio del producto en una unidad.
                value["precio"] = float(value["precio"]) - producto.Precio
                # Si la cantidad es menor que 1, elimina el producto del carro.
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        # Guarda los cambios en la sesión.
        self.guardar_carro()

    # Método para limpiar el carro, eliminando todos los productos.
    def limpiar_carro(self):
        # Reemplaza el carro en la sesión con un diccionario vacío.
        self.session["carro"] = {}
        # Marca la sesión como modificada para asegurarse de que se guarde.
        self.session.modified = True