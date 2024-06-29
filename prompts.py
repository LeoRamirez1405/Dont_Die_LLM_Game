INITGAME = """Eres un creador de situaciones de un juego. Debes crear un mundo donde un jugador deba superar 
ciertos niveles de acuerdo con el mundo que creaste (Puede ser un mundo de fantasía, ficción, apocalíptico, terror u otro género cualquiera).
El objetivo es que en dicho mundo se presenten progresivamente desafíos que el jugador deba superar.
A continuación crea una historia pequeña del mundo."""

def player_init_op(world):
    return f"""Dado el mundo creado: {world}
Crea 3 tipos diferentes de personajes los cuales podrían interactuar con el mundo. Estos personajes deben ser simples
y poder ir adquiriendo habilidades con el tiempo. El formato a devolver debe ser el siguiente:
Ejemplos:
Arquero: Un aficionado al uso de armas a distancia sin mucha experiencia
Mago: Posee el don de hacer cosas sobrenaturales pero no sabe controlarlo
Sobreviviente: Capaz de dar un esfuerzo extra en los momentos cruciales"""

def player_init_stats(world,player,params):
    return f"""Dado esta descripción de un personaje de videojuego: {player} y
esta descripción del mundo: {world} has una asignación a cada uno de estos parámetros: {params}. Cada parámetro
debe tener un número entre 1 y 12.
La respuesta debe tener este formato:
<habilidad> = <cantidad>
Ejemplo:
Vida = 5
Fuerza = 7
"""

def challenge(world, history, player, features):    
    return f"""En el mundo: {world}. Dado el siguiente historial de desafios: {history} y el siguiente jugador: {player} con las caracteristicas siguientes: {features}
genera un nuevo desafio para el jugador de forma tal que el mismo deba utilizar su ingenio para luchar y sobrevivir."""

def post_action_survive(situation,world, response):
    return f"""Dada la siguiente situación: {situation} en este mundo: {world} y esta respuesta del jugador {response}. Valora esta respuesta del jugador y responde 1 (en caso
de que dicha acción lo haría sobrevivir) o 0 (En caso contrario)."""

def post_action_appropriate(situation,world, response, features):
    return f"""Dada la siguiente situación: {situation} en este mundo: {world}, esta respuesta del jugador {response} y las habilidades del mismo {features}. Valora esta respuesta del jugador y responde 1 (en caso
de que dicha acción se corresponde con lo que puede hacer el jugador con los skills que tiene y en el mundo en el que se encuentra) o 0 (En caso contrario)."""

def post_action_development(challenge, world, action, player, features):
    return f"""Di como se desenvolvió el challenge {challenge} que ocurre en este mundo {world} cuya respuesta del jugador fue {action}. Dime que obtuvo el jugador {player} segun su acción tomada en esta situación, ten en cuenta que la respuesta que quiero
es para actualizar las estadísticas del jugador. Sus caracteristicas son las siguientes {features}."""
    
    