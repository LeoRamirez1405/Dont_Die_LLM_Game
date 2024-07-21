import streamlit as st
from Game import Game
import json

def main():
    # Configuración inicial de la página
    st.set_page_config(page_title="Don't Die", page_icon="👻")

    # Título y subtítulo
    st.markdown("# Don't Die 👻: Sobrevive o Muere Intentando")
    st.markdown("## Un Juego de Aventura en el Umbral de la Muerte")

    # Muestra el mundo del juego
    st.write("Aquí está el mundo del juego:")
    st.write(game.world)

    # Opciones de selección de personajes
    character_options = game.get_players_to_select()
    selected_character = st.selectbox("Elige tu personaje:", character_options)

    # Botón para iniciar el juego
    if st.button("Comenzar a jugar"):
        st.success(f"Iniciando el juego con {selected_character}...")
       
        game.select_player(selected_character)
        json.dump({'game': game}, './game')
    
    # Botón para regenerar el mundo
    if st.button("Regenerar mundo"):
        st.info("Regenerando el mundo...")
        # Regenera el mundo llamando al constructor de la clase Game
        game = Game()
        json.dump({'game': game}, './game')
        # Actualiza el estado del mundo en la UI
        st.write(game.world)

if __name__ == "__main__":
    # game = Game()  # Crea una instancia inicial del juego
    try:
        game = Game(json.load('./game')['game'])
    except:
        game = Game()
        json.dump({'game': game}, './game')
        
    st.session_state.game = game
    st.session_state.history = []
    main()

# import streamlit as st
# from Game import Game
# import json

# def run():
#     import streamlit as st

#     # Configuración inicial de la página
#     st.set_page_config(page_title="Don't Die", page_icon="👻")

#     # Título centrado y con un tamaño específico
#     st.markdown("<h1 style='text-align: center; font-size: 30px;'>Don't Die 👻: Sobrevive o Muere Intentando</h1>", unsafe_allow_html=True)

#     # Subtítulo opcionalmente centrado y con un tamaño diferente
#     st.markdown("<h2 style='text-align: center; font-size: 20px;'>Un Juego de Aventura en el Umbral de la Muerte</h2>", unsafe_allow_html=True)
    
#     try:
#         game = Game(json.load('./game')['game'])
#     except:
#         game = Game()
#         json.dump({'game': game}, './game')

#     if "history" not in st.session_state:
#         st.session_state.history = []    
    
#     if len(game.history) == 0:
#         world = game.world
#         st.write(world)
    
#     msg = st.chat_input()
    
#     if msg:
#         game.
#     else:
        
    
#     with st.chat_message("assistant"):
#         st.write("World 🌎")
#         st.write(game.world)
    
#     with st.chat_message("user"):
#         st.write(msg)
        
# def store(role, content):
#     st.session_state.history.append(dict(content=content, role=role))

