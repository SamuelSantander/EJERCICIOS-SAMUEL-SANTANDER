#Dado un listado de tuplas (producto, categoría), agrupa los productos por categoría usando un diccionario de listas. 
productos = [
    ("laptop", "tecnologia"),
    ("mouse", "tecnologia"),
    ("manzana", "alimentos"),
    ("pan", "alimentos"),
    ("camisa", "ropa")
]

def agrupar_categoria(lista_productos):
    categorias = {}
    for producto, categoria in lista_productos: 
        if categoria not in categorias:
            categorias[categoria] = []
            categorias[categoria].append(producto)
    return categorias

resultado = agrupar_categoria(productos)
print(resultado)