INITGAME = """Eres un creador de situaciones de un juego. Debes crear un mundo donde un jugador deba superar 
ciertos niveles de acuerdo con el mundo que creaste (Puede ser un mundo de fantasía, ficción, apocalíptico, terror u otro género cualquiera).
El objetivo es que en dicho mundo se presenten progresivamente desafíos que el jugador deba superar.
A continuación crea una historia pequeña del mundo. Solo crea la historia, no agregues preguntas ni texto para dialogar. Solo el inicio de una historia en español"""

def player_init_op(world):
    return f"""Dado el mundo creado: {world}
Crea 3 tipos diferentes de personajes los cuales podrían interactuar con el mundo. Estos personajes deben ser simples
y poder ir adquiriendo habilidades con el tiempo. El formato a devolver debe ser el siguiente, un diccionario de python:\n
"""+"""
Ejemplos: 
{
    "Explorador": "Un aventurero experimentado en la exploración de la superficie",
    "Ingeniero": "Un experto en tecnología capaz de reparar y mejorar máquinas",
    "Luchador": "Un guerrero entrenado en el combate cuerpo a cuerpo"
}

{
    "Arqueologo": "Un experto en la búsqueda y análisis de antigüedades valiosas",
    "Hechicera": "Una maestra de las artes mágicas, capaz de manipular elementos y energías",
    "Navegante": "Un experto marinero, hábil en la navegación y supervivencia en alta mar"
}

Solo devuelveme el diccionario de los personajes, sin texto adicional
"""
def user_response_option(options, response):
    return f"""Dado estas opciones {options} y esta respuesta {response}, devuelve el nombre y la descripcion de la opcion escogida.
            No agregues texto adicional a la respuesta. Solo devuelveme lo que te pido"""
            
def player_init_stats(world,player,params):
    return f"""Dado esta descripción de un personaje de videojuego: {player} y
esta descripción del mundo: {world} has una asignación a cada uno de estos parámetros: {params}. Cada parámetro
debe tener un número entre 0 y 3 Excepto Type, que es el tipo del jugador.
La respuesta debe tener estrictamente este formato. Cualquier otro formato o texto fuera de la siguiente estructuta sera una mala respuesta:
<habilidad> = <cantidad>
Ejemplo:
Vida = 2
Fuerza = 1

Solo da la respuesta de la asignación dentro de estas señales: 
<asignacion></asignacion>. Ejemplo:

<asignacion>
Type = <tipo>
Vida = 2
Fuerza = 1
</asignacion>

Solo devuelve la asignacion de los parametros del jugador. No des texto adicional, ni siquiera el texto que te acabo de dar
"""

def challenge(world, history, player):    
    return f"""En el mundo: {world}. Dado la siguiente historia: {history} y el siguiente jugador: {player}
genera un desafio a continuacion acorde a la historia que tenga sentido en la escena para el jugador de forma tal que el mismo deba utilizar su ingenio para luchar y sobrevivir. Solo devuelve el desafío actual, ninguna información extra
Genera la situación. 
Ejemplo:
<response>


Solo devuelve lo que generes luego de response pero sin devolver las etiquetas <response>, nada extra y en español
"""

def post_action_survive(situation,world, response):
    return f"""Dada la siguiente situación: {situation} en este mundo: {world} y esta respuesta del jugador {response}. Valora esta respuesta del jugador y di si el jugador puede hacer o no
lo que respondio teniendo en cuenta el mundo en el que se encuentra y las caracteriticas del mismo, para saber si es valida la accion o no. responde 1 (en caso
de que dicha acción lo haría sobrevivir) o 0 (En caso contrario o en caso de que la accion no se corresponde con lo apto por el mundo en el que se encuentra pues se quiere que sea lo mas acorde posible)."""

def post_action_appropriate(situation,world, response, features):
    return f"""Dada la siguiente situación: {situation} en este mundo: {world}, esta respuesta del jugador {response} y las habilidades del mismo {features}. Valora esta respuesta del jugador, ten en cuenta las estadisticas del jugador y el tipo del mismo. 
Ten en cuenta que si es de un tipo las actividades que haga deben ser exclusivamente de ese tipo de jugador y que las estadisticas son para tener una idea de cuan bueno puede ser el jugador en ciertas areas y asi saber sus limitaciones a la hora de actuar.
Sabiendo esto y responde 1 (en caso
de que dicha acción se corresponde con lo que puede hacer el jugador con los skills que tiene y en el mundo en el que se encuentra) o 0 (En caso contrario)"""

def post_action_development(challenge, world, action):
    return f"""Di como se desenvolvió el challenge {challenge} que ocurre en este mundo {world} cuya respuesta del jugador fue {action}. Dime que obtuvo el jugador segun su acción tomada en esta situación, ten en cuenta que la respuesta que quiero
es para actualizar las estadísticas del jugador. ten en cuenta que <int> debe ser un numero del -5 >= <int> <=5 y si el jugador pierde por alguna casualidad, la salud debe ser 0. Ten en cuenta que debe ser un desafio,
da igual lo que haya pasado, haz que el desenvolvimiento de a accion tenga un giro inesperado y el jugador pierda y gane habilidades en funcion de su creatividad, que no todo sea positivo
. Esto anteriormente dicho debe verse reflejado en las <update-habilidades>. Solo devuelve lo que te pido, ningun texto adicional. devuelve la respuesta en este formato:
<desenvolvimiento de la situación>
<update-habilidades> en el formato:"""+"""
{'strength': <int>, 'intelligence': <int>, 'agility': <int>, 'health': <int>, 'luck': <int>}

"""
    
def bad_result(situation, world, action, features):
    return f"""Dada la siguiente situación: {situation} en este mundo: {world}, esta respuesta del jugador {action} y las habilidades del mismo {features}. Devuelva una historia donde el personaje del juagador sufre un revés"""

def obtain_item_post_action(challenge, world, action, player, features):
    pass

def obtain_weapon_post_action(challenge, world, action, player, features):
    pass

def obtain_staistics_post_action(challenge, world, action, player, features):
    pass


def loss_item_post_action_(challenge, world, action, player, features):
    pass

def loss_weapon_post_action(challenge, world, action, player, features):
    pass 

def loss_staistics_post_action(challenge, world, action, player, features):
    pass