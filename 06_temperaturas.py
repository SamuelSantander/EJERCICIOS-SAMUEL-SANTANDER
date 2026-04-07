#Almacena temperaturas semanales por ciudad y encuentra la más caliente y la más fría de la semana.

def analizar_temp(datos):
    temperatura_max = float("-inf")
    temperaturas_min = float("inf")

    ciudad_max = ""
    ciudad_min = ""
    for ciudad, lista_temperaturas in datos.items():
        max_ciudad = max(lista_temperaturas)
        min_ciudad = min(lista_temperaturas)

        if max_ciudad > temperatura_max:
            temperatura_max = max_ciudad
            ciudad_max = ciudad

        if min_ciudad < temperaturas_min:
            temperatura_min = min_ciudad
            ciudad_min = ciudad

    print("Ciudad mas caliente", "=", temperatura_max, "C")
    print("Ciudad mas fria", ciudad_min, "=", temperatura_min, "C")


temperaturas = {
    "New York": [20, 10, 25, 9, 13],
    "Sidney": [26, 16, 12, 30, 22]
}


analizar_temp(temperaturas)