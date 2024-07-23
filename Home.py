import streamlit as st
from src.Game import Game
import json, os

st.set_page_config(page_title="Don't Die", page_icon="👻")
st.markdown("# Don't Die 👻: Sobrevive o Muere Intentando")
# st.markdown("## Un Juego de Aventura en el Umbral de la Muerte")

game = Game()

def delete_object(object):
    path = 'data/'
    try:
      os.remove(f'{path}{object}.json')
      print("Archivo borrado correctamente.")
    except FileNotFoundError:
      print("Error: El archivo no se encuentra.")

try:
    with open('data/world.json', 'r') as f:
        data = json.load(f)
        world = game.world = data['world']
    st.success('Loaded game')
except:
    # Borrar los jugadores anteriores
    delete_object('players_options')
    
    game = Game()
    world = game.generate_world()
    with open('data/world.json', 'w') as f:
        json.dump({'world': world}, f)
    
    st.session_state.game = game
        
    # history = st.session_state.history = []
    # situation = st.session_state.situation = ''
    st.success('Created game')

# # Muestra el mundo del juego
st.write(world)

# Botón para regenerar el mundo
if st.sidebar.button("Regenerar mundo"):
    delete_object('world')
    delete_object('players_options')
    delete_object('game_state')
    
    st.rerun()
    
st.stop()
