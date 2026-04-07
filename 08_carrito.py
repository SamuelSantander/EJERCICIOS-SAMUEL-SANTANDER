#Simula un carrito de compras con funciones para agregar productos, aplicar descuentos y generar el total a pagar. 
carrito = {}


#funcion agregar productos
def agregar_producto(nombre, precio):
    carrito[nombre] = precio
    print("Producto Agregado", nombre)

#mostrar carrito
def mostrar_carrito():
    print("\nCarrito de Compras")
    for producto, precio in carrito.items():
        print(producto, "-", precio)

#Calcular total
def calcular_total():
    total = sum(carrito.values())
    return total

#Aplicar descuento
def aplicar_descuento (porcentaje):
    total = calcular_total()
    descuento = total * (porcentaje/100)
    total_final = total - descuento
    print("total antes del descuento: ", total)
    print("descuento aplicado: ", descuento)
    print("total a pagar: ", total_final)

agregar_producto("Laptop", 3000)
agregar_producto("Mouse", 160)
agregar_producto("Teclado", 320)

mostrar_carrito()
print("total: ", calcular_total())
aplicar_descuento(10)

#ARGUMETOS EN FUNCIONES 