INITGAME = """Eres un creador de situaciones de un juego. Debes crear un mundo donde un jugador deba superar 
ciertos niveles de acuerdo con el mundo que creaste (Puede ser un mundo de fantasía, ficción, apocalíptico, terror u otro género cualquiera).
El objetivo es que en dicho mundo se presenten progresivamente desafíos que el jugador deba superar.
A continuación crea una historia pequeña del mundo."""

PLAYERINIT_OP = f"""Dado el mundo creado: {}
Crea 3 tipos diferentes de personajes los cuales podrían interactuar con el mundo. Estos personajes deben ser simples
y poder ir adquiriendo habilidades con el tiempo. El formato a devolver debe ser el siguiente:
Ejemplos:
Arquero: Un aficionado al uso de armas a distancia sin mucha experiencia
Mago: Posee el don de hacer cosas sobrenaturales pero no sabe controlarlo
Sobreviviente: Capaz de dar un esfuerzo extra en los momentos cruciales"""

def player_init_stats(player,):
    return f"""Dado esta descripción de un personaje de videojuego: {player} y
esta descripción del mundo: {INITGAME} has una asignación a cada uno de estos parámetros: {}. Cada parámetro
debe tener un número entre 1 y 12.
La respuesta debe tener este formato:
<habilidad> = <cantidad>
Ejemplo:
Vida = 5
"""

def challenge(history, player, features):    
    return f"""En el mundo: {INITGAME}. Dado el siguiente historial de desafios: {history} y el siguiente jugador: {player} con las caracteristicas siguientes: {features}
genera un nuevo desafio para el jugador de forma tal que el mismo deba utilizar su ingenio para luchar y sobrevivir."""