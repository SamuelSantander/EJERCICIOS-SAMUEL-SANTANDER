#Usa una lista de tuplas (nombre, nota) y una función que devuelva solo los estudiantes aprobados (nota ≥ 3.0). 
def evaluar_estudiantes (notas):
    aprobados = []
    no_aprobados = []
    for nombre, nota in notas:
        if nota >= 3:
           aprobados.append(nombre)
        else:
            no_aprobados.append(nombre)
    print("Aprobados", aprobados)
    print("No Aprobados", no_aprobados)

notas = [
    ("Ana", 4),
    ("Samuel", 5),
    ("Diego", 3.2),
    ("Lorena", 2),
    ("Alex", 1)
]

evaluar_estudiantes(notas)