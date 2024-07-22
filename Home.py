import streamlit as st
from src.Game import Game
import json, os

st.set_page_config(page_title="Don't Die", page_icon="👻")
st.markdown("# Don't Die 👻: Sobrevive o Muere Intentando")
# st.markdown("## Un Juego de Aventura en el Umbral de la Muerte")

game = Game()

def delete_object():
    path = 'data/'
    try:
      os.remove(f'{path}players_options.json')
      print("Archivo borrado correctamente.")
    except FileNotFoundError:
      print("Error: El archivo no se encuentra.")

try:
    with open('data/world.json', 'r') as f:
        data = json.load(f)
        world = game.world = data['world']
    st.success('Loaded game')
except:
    game = Game()
    world = game.generate_world()
    with open('data/world.json', 'w') as f:
        json.dump({'world': game.world}, f)
        
    # Borrar los jugadores anteriores
    delete_object()
    
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
    
    delete_object()
    
    st.session_state.game = game
    st.write(game.world)
    
st.stop()
