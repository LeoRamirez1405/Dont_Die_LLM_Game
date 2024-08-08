import streamlit as st
from src.Game import Game
from src.prompts import *
from src.game_objects import character
import json

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
    options: dict = game.options()
    # print(type(options))
    
    players_options_list = [k+': '+v+'\n' for k, v in options.items()]
    print(players_options_list)
    character_options_str = ''
    for index, opt in enumerate(players_options_list):
        # print(opt)
        character_options_str += f'{index+1}. {opt}.\n' 

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
    
def save_player(player: character):
    with open('data/player.json', 'w') as f:
        json.dump({
        "player": {
        "type": player.type,
        "strength": player.strength,
        "intelligence": player.intelligence,
        "agility": player.agility,
        "health": player.health,
        "luck": player.luck}
    }, f)
    

# Opciones de selección de personajes
st.write(character_options_str)

index_selected_character = st.selectbox("Elige tu personaje:", [i+1 for i in range(3)])
selected_character = players_options_list[index_selected_character - 1]

# Botón para iniciar el juego
if st.sidebar.button("Comenzar a jugar"):
    if not selected_character:
        st.warning('You need to select a player first')
        st.stop()
    
    print('selected_character: ', selected_character)
    player: character = game.select_player(selected_character)
    st.session_state.game = game
    
    st.success(f"Iniciando el juego con: \n {str(player)}...")
    
    save_player(player)
    
    st.success("Done. Puede comenzar el juego. Vaya a la página \'Start Game\' ")
