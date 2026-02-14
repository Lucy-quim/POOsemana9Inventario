from Modelos.productos import Producto
from Servicios.inventario import Inventario

def menu():
    mi_inventario = Inventario()
    
    while True:
        print("\n--- GESTIÓN DE INVENTARIO MI TIENDA LPQ ---")
        print("1. Añadir producto nuevo")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID (único): ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                prec = float(input("Precio: "))
                
                exito, msg = mi_inventario.agregar_producto(Producto(id_p, nom, cant, prec))
                print(msg)
            except ValueError:
                print("Error: Cantidad y Precio deben ser valores numéricos.")

        elif opcion == "2":
            id_p = input("Ingrese el ID del producto a eliminar: ")
            if mi_inventario.eliminar_producto(id_p):
                print("Producto eliminado correctamente.")
            else:
                print("Error: ID no encontrado.")

        elif opcion == "3":
            id_p = input("Ingrese ID del producto a actualizar: ")
            print("Deje en blanco si no desea modificar el campo.")
            cant_in = input("Nueva cantidad: ")
            prec_in = input("Nuevo precio: ")
            
            n_cant = int(cant_in) if cant_in else None
            n_prec = float(prec_in) if prec_in else None
            
            if mi_inventario.actualizar_producto(id_p, n_cant, n_prec):
                print("Producto actualizado con éxito.")
            else:
                print("Error: No se encontró el ID.")

        elif opcion == "4":
            busqueda = input("Nombre del producto a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(busqueda)
            if resultados:
                print("\nResultados encontrados:")
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            todos = mi_inventario.listar_productos()
            if not todos:
                print("\nEl inventario está vacío.")
            else:
                print("\nLISTADO COMPLETO:")
                for p in todos: print(p)

        elif opcion == "6":
            print("Salio del sistema mi TIENDA LPQ . ¡Vuelva pronto!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()