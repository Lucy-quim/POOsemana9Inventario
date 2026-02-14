from Modelos.productos import Producto
from Servicios.inventario import Inventario

def menu():
    sistema = Inventario()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID único: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            exito, msj = sistema.añadir_producto(Producto(id_p, nom, cant, prec))
            print(msj)

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            if sistema.eliminar_producto(id_p):
                print("Eliminado correctamente.")
            else:
                print("No se encontró el ID.")

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            n_cant = input("Nueva cantidad (deje vacío para no cambiar): ")
            n_prec = input("Nuevo precio (deje vacío para no cambiar): ")
            
            c = int(n_cant) if n_cant else None
            p = float(n_prec) if n_prec else None
            
            if sistema.actualizar_producto(id_p, c, p):
                print("Actualizado con éxito.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nom = input("Escriba el nombre a buscar: ")
            resultados = sistema.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            lista = sistema.obtener_todos()
            if not lista:
                print("Inventario vacío.")
            for p in lista: print(p)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()