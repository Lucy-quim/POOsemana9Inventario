class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def set_nombre(self, nombre): self._nombre = nombre
    def get_cantidad(self): return self._cantidad
    def set_cantidad(self, cantidad): self._cantidad = cantidad
    def get_precio(self): return self._precio
    def set_precio(self, precio): self._precio = precio

    def __str__(self):
        return f"ID: {self._id} | {self._nombre} | Cant: {self._cantidad} | Precio: ${self._precio:.2f}"