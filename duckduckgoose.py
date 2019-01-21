def duckduckgoose(jugador_goose, posicion_jugador_goose):
    lista_jugadores = list(jugador_goose)
    posicion_jugador_goose = int(posicion_jugador_goose)
    goose = jugador_goose[posicion_jugador_goose]
    return (goose, posicion_jugador_goose)


print (duckduckgoose (['Alicia', 'Blanca', 'Ines', 'Angelica', 'Pablo'], 1))
