def juego_substrings(texto):
    vocales = "aeiou"
    jugador_A = [] 
    jugador_B = []  

    for i in range(len(texto)):
        for j in range(i+1, len(texto)+1):
            sub = texto[i:j]
            if texto[i] in vocales:
                jugador_A.append(sub)
            else:
                jugador_B.append(sub)

    def contar_repeticiones(lista):
        resultado = []
        usados = set()
        for sub in lista:
            if sub not in usados:
                cantidad = lista.count(sub)
                resultado.append((sub, cantidad))
                usados.add(sub)
        return resultado

    frecuencia_A = contar_repeticiones(jugador_A)
    frecuencia_B = contar_repeticiones(jugador_B)

    total_A = len(jugador_A)
    total_B = len(jugador_B)

    if total_A > total_B:
        ganador = "Jugador A"
        lista_ganadora = jugador_A
        cantidad_ganadora = total_A
    elif total_B > total_A:
        ganador = "Jugador B"
        lista_ganadora = jugador_B
        cantidad_ganadora = total_B
    else:
        ganador = "Empate"
        lista_ganadora = []
        cantidad_ganadora = total_A

    return {
        "ganador": ganador,
        "substrings": lista_ganadora,
        "cantidad": cantidad_ganadora,
        "frecuencia_A": frecuencia_A,
        "frecuencia_B": frecuencia_B
    }

resultado = juego_substrings("banana")
print("Ganador:", resultado["ganador"])
print("Cantidad:", resultado["cantidad"])
print("Lista ganadora:", resultado["substrings"])
print("Frecuencia Jugador A:", resultado["frecuencia_A"])
print("Frecuencia Jugador B:", resultado["frecuencia_B"])