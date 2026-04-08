from funcion import mostrar_productos
from funcion import agregar_producto
from funcion import comprar_producto
from funcion import ver_carrito


def menu():
    while True:
        print("\n===== SUPERMERCADO =====")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Comprar producto")
        print("4. Ver carrito")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            agregar_producto()

        elif opcion == "3":
            comprar_producto()

        elif opcion == "4":
            ver_carrito()

        elif opcion == "5":
            print("Gracias por usar el supermercado")
            break

        else:
            print("Opción inválida")

menu()