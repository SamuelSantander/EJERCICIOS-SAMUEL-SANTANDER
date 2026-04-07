# Crea funciones que reciban una lista de notas y calculen el promedio, la nota más alta y la nota más baja. 
def sumar_notas (notas):
    resultado = sum(notas)
    return resultado


def nota_alta (notas):
    return max(notas)



def nota_baja (notas):
    return min(notas)


notas = [4, 8, 9, 6, 2]
total = sumar_notas(notas)
print("-----Promedio-------")
print(total/len(notas))

print("-------Nota Alta-------")
print(nota_alta (notas))

print("------Nota Mas Baja--------")
print(nota_baja(notas))

