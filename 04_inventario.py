#Gestiona un inventario donde cada producto tiene nombre, precio y cantidad. Calcula el valor total del inventario. 
producto1 = {"nombre": "Cuaderno", "precio": 12000, "cantidad": 10}
producto2 = {"nombre": "Lápiz", "precio": 2500, "cantidad": 30}
producto3 = {"nombre": "Borrador", "precio": 300, "cantidad": 20}

def calcular_valor_inventario(producto1, producto2, producto3):
    total1 =producto1["precio"] * producto1["cantidad"]
    total2 = producto2["precio"] * producto2["cantidad"]
    total3 = producto3["precio"] * producto3["cantidad"]   
    total_final = total1 + total2 + total3
    return total_final


resultado = calcular_valor_inventario(producto1, producto2, producto3)
print(resultado)