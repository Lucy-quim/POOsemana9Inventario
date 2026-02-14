class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__stock = cantidad
        self.__precio = precio

    # Getters y Setters
    @property
    def id(self): return self.__id

    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @property
    def cantidad(self): return self.__stock
    @cantidad.setter
    def cantidad(self, valor): self.__stock = valor

    @property
    def precio(self): return self.__precio
    @precio.setter
    def precio(self, valor): self.__precio = valor

    def __str__(self):
        return f"[{self.__id}] {self.__nombre.ljust(15)} | Stock: {str(self.__stock).rjust(5)} | Precio: ${self.__precio:,.2f}"
