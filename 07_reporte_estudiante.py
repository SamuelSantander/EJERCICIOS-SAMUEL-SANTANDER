#Convierte notas numéricas a letras (A, B, C, D, F) usando tuplas como rangos y devuelve un reporte por estudiante. 
rangos = [
    (90, 100, "A"),
    (80, 89, "B"),
    (70, 79, "C"),
    (60, 69, "D"),
    (0, 59, "F")
]

estudiantes = [
    ("Samuel", 100),
    ("Lorena", 89),
    ("Alvaro", 57),
    ("Peter", 70),
    ("Jairo", 20)    
]

def convertir_nota(nota, rangos):
    for minimo, maximo, letra in rangos:
        if minimo <= nota <= maximo:
            return letra
        
def generar_reportes(estudiantes, rangos):
    for nombre, nota in estudiantes:
        letra = convertir_nota(nota, rangos)
        print(nombre, "- nota: ", nota, "- calificacion: ", letra)

generar_reportes(estudiantes, rangos)