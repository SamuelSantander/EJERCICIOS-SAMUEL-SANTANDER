#Implementa una agenda simple con funciones para agregar, buscar y eliminar contactos usando un diccionario. 
agenda = {
    "Samuel": "5883832",
    "Jose": "4463636",
    "Leonor": "377777",
    "Luz": "7473848"
}

def agregar_contacto (nombre, telefono):
    agenda[nombre] = telefono
    print("Contacto Agregado")

def buscar_contacto (nombre):
    if nombre in agenda:
        print(nombre, ": ", agenda[nombre])
    else:
        print("Contacto No Encontrado")

def eliminar_contacto (nombre):
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto Eliminado")
    else:
        print("Contacto No Existe")

agregar_contacto("Lorena", "6476875")
buscar_contacto("Samuel")
eliminar_contacto("Jose")

print(agenda)