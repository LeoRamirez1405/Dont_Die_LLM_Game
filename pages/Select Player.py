import streamlit as st
from src.Game import Game
from src.prompts import *
import json

def get_players_options(options_list):
    players_options = []
    
    # print(f'get_players_options: {len(options_list)}')
    opt = 0
    while opt < len(options_list) - 1:
        # print('OPTION')
        # print(f'{options_list[opt]} \n {options_list[opt+1]}')
        players_options.append(f'{options_list[opt]} \n {options_list[opt+1]}')
        opt += 2

    return players_options

# def extract_characters(description: str):
#     # Dividir la cadena en líneas separadas por "\n"
#     lines = description.split('\n')
    
#     # Inicializar la lista que contendrá los personajes
#     characters = []
    
#     # Recorrer cada línea
#     for line in lines:
#         # Dividir la línea en dos partes: el nombre del personaje y la descripción
#         partes = line.split(': ', 1)
        
#         # Si hay al menos dos partes, agregar a la lista
#         if len(partes) == 2:
#             personaje = partes[1].strip()
#             characters.append(personaje)
    
#     return characters

game = Game()

# Loading the world
try:
    with open('data/world.json', 'r') as f:
        data = json.load(f)
        game.world = data['world']
        world = game.world
except Exception as e:
    st.error(e)
    st.warning('You need to generate the world first')
    st.stop()
    
# Loading the players options
try:
    with open('data/players_options.json', 'r') as f:
        data = json.load(f)
        character_options_str = data['character_options_str']
        players_options_list = data['players_options_list']
        
    st.success('Loaded players')
    
except:
    character_options_str = game.get_players_to_select()
    players_options_list = character_options_str.split('\n')
    # players_options_list = get_players_options(character_options_str.split('\n'))

    with open('data/players_options.json', 'w') as f:
        json.dump({
            'character_options_str': character_options_str,
            'players_options_list': players_options_list}, f) 
    player = None
    
    st.success('Generated players')
    
try:
    with open('data/player.json', 'r') as f:
            data = json.load(f)
            player = data['player']
except:
    player = None

# Opciones de selección de personajes
st.write(character_options_str)

index_selected_character = st.selectbox("Elige tu personaje:", [i+1 for i in range(3)])
# st.write(len(players_options_list))
# st.write(f"index_selected_character: {index_selected_character - 1}")
selected_character = players_options_list[index_selected_character - 1]

# Botón para iniciar el juego
if st.sidebar.button("Comenzar a jugar"):
    if not selected_character:
        st.warning('You need to select a player first')
        st.stop()
    
    player = game.select_player(selected_character)
    st.session_state.game = game
    
    st.success(f"Iniciando el juego con: \n {selected_character[:4]}...")
    
    with open('data/player.json', 'w') as f:
        json.dump({'player': player}, f)
    
    st.success("Done")
