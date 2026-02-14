from Modelos.productos import Producto

class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        # Validar que el ID sea único
        if any(p.id == producto.id for p in self.__productos):
            return False, f"Error: Ya existe un producto con el ID {producto.id}."
        
        self.__productos.append(producto)
        return True, "Producto agregado exitosamente."

    def eliminar_producto(self, id_producto):
        for p in self.__productos:
            if p.id == id_producto:
                self.__productos.remove(p)
                return True
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.__productos:
            if p.id == id_producto:
                if nueva_cantidad is not None: p.cantidad = nueva_cantidad
                if nuevo_precio is not None: p.precio = nuevo_precio
                return True
        return False

    def buscar_por_nombre(self, nombre_buscado):
        # Coincidencia parcial e insensible a mayúsculas
        return [p for p in self.__productos if nombre_buscado.lower() in p.nombre.lower()]

    def listar_productos(self):
        return self.__productos