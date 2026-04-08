productos = {
    1: ("Arroz", 2500, 10),
    2: ("Leche", 3000, 8),
    3: ("Huevos", 12000, 5)
}

carrito = []


def mostrar_productos():
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for codigo, producto in productos.items():
        nombre, precio, cantidad = producto
        print(f"{codigo}. {nombre} - ${precio} - Stock: {cantidad}")


def agregar_producto():
    codigo = int(input("Código: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    productos[codigo] = (nombre, precio, cantidad)

    print("Producto agregado")


def comprar_producto():
    mostrar_productos()

    codigo = int(input("Código del producto: "))

    if codigo in productos:
        nombre, precio, cantidad = productos[codigo]

        if cantidad > 0:
            carrito.append((nombre, precio))
            productos[codigo] = (nombre, precio, cantidad - 1)
            print("Producto agregado al carrito")
        else:
            print("Sin stock")
    else:
        print("Producto no existe")


def ver_carrito():
    print("\n--- CARRITO ---")

    total = 0

    for producto in carrito:
        nombre, precio = producto
        print(f"{nombre} - ${precio}")
        total += precio

    print(f"\nTotal: ${total}")