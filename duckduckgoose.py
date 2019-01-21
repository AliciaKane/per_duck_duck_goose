def duckduckgoose(jugador_goose, posicion_jugador_goose):
    lista_jugadores = list(jugador_goose)
    posicion_jugador_goose = int(posicion_jugador_goose)
    goose = lista_jugadores[posicion_jugador_goose]
    return (goose, posicion_jugador_goose)

oca = duckduckgoose (['Alicia', 'Blanca', 'Ines', 'Angelica', 'Pablo'], 1)[0]
pato = duckduckgoose (['Alicia', 'Blanca', 'Ines', 'Angelica', 'Pablo', 'Maria'], 1)[1]
print ("La oca sera: ", oca, "y su posicion es: ", pato)
