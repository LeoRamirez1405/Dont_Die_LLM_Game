import streamlit as st
from src.Game import Game
import json

st.set_page_config(page_title="Don't Die", page_icon="👻")
st.markdown("# Don't Die 👻: Sobrevive o Muere Intentando")
# st.markdown("## Un Juego de Aventura en el Umbral de la Muerte")

try:
    game: Game = st.session_state.game
    world = game.world
    
    history = st.session_state.history
    situation = st.ssesion_state.situation
    st.success('Loaded game')
except:
    game = Game()
    world = game.generate_world()
    with open('data/world.json', 'w') as f:
        json.dump({'world': game.world}, f)
        
    st.session_state.game = game
        
    history = st.session_state.history = []
    situation = st.session_state.situation = ''
    st.success('Created game')

# # Muestra el mundo del juego
st.write(world)

# Botón para regenerar el mundo
if st.sidebar.button("Regenerar mundo"):
    st.info("Regenerando el mundo...")
    # Regenera el mundo llamando al constructor de la clase Game
    game.generate_world()
    
    with open('data/world.json', 'w') as f:
        json.dump({'world': game.world}, f)
    
    st.session_state.game = game
    st.write(game.world)
    
st.stop()
