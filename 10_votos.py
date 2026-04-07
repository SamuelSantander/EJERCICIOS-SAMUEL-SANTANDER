#Registra votos de una lista de candidatos, detecta votos inválidos y determina el ganador con su porcentaje. 
candidatos = ["Samuel", "Jose", "Eduardo"]
votos = ["Samuel", "Jose", "Samuel", "Alex", "Eduardo", "Jose", "Samuel", "Jose", "Samuel", "Alex", "Eduardo", "Jose"]

def contar_votos(candidatos, votos):
    conteo = {candidato: 0 for candidato in candidatos}
    votos_invalidos = 0
    for voto in votos:
        if voto in candidatos:
            conteo[voto] += 1
        else:
            votos_invalidos += 1
    return conteo, votos_invalidos

def calcular_ganador(conteo):
    total_votos = sum(conteo.values())
    ganador = max(conteo, key=conteo.get)
    votos_ganador = conteo[ganador]
    porcentaje = (votos_ganador / total_votos) * 100
    return ganador, porcentaje

conteo, invalidos = contar_votos(candidatos, votos)
ganador, porcentaje = calcular_ganador(conteo)
print("Conteo de Votos: ", conteo)
print("Votos invalidos: ", invalidos)
print("ganador: ", ganador)
print("porcentaje: ", round(porcentaje, 2), "%")