import streamlit as st
from src.Game import Game
from src.game_objects import character
from src.prompts import *
from src.API_Fireworks import UserType
import json
from enum import Enum

st.set_page_config(page_title="Don't Die", page_icon="👻")
class files(Enum):
    Player = 'player'
    Game_State = 'game_state'
    World = 'world'
    History = 'history'
    Situation = 'situation'
    Response = 'response'
    
class state_msg(Enum):
    warning = 0
    error = 1
    success = 2
    none = 3

def save(json_file, file):
    try:
        with open(f'data/{file}.json', 'w') as f:
            json.dump(json_file, f)
    except Exception as e:
        print(f'save error: {e}')
                
def get_palyer(player_json):
    return character(
        player_json['type'],
        player_json['strength'],
        player_json['intelligence'],
        player_json['agility'],
        player_json['health'],
        player_json['luck']
    )

game = Game()

try:    
    with open('data/player.json', 'r') as f:
        data = json.load(f)
        game.player = get_palyer(data['player'])          
except Exception as e:
    st.warning('You need to generate the world and select a player first')
    # st.error(e)
    st.stop()
    
try:  
    with open('data/history.json', 'r') as f:
        data = json.load(f)  
        st.session_state.history = data['history']
    # print('Loaded history')
except:
    st.warning('Antes debe generar un mundo y seleccionar un jugador.')
    st.stop()
        
def show_history():
    print('Show History')
    
    if game.player:
        player_info = f"""
        **Jugador**: \n\n
        *Tipo*: {game.player.type},
        *🦾Fuerza*: {game.player.strength},
        *🧠 Inteligencia*: {game.player.intelligence}, 
        *🏃‍♀️Agilidad*: {game.player.agility},
        *💊Salud*: {game.player.health},
        *🍀Suerte*: {game.player.luck}
        """
        st.write(player_info)

    # with st.chat_message('assistant'):
    #     st.write(st.session_state.history[0])
    for msg in st.session_state.history:
        with st.chat_message(msg['role']):
            if msg['state'] == state_msg.error.value:
                st.error(msg['content'])
            elif msg['state'] == state_msg.warning.value:
                st.warning(msg['content'])
            elif msg['state'] == state_msg.success.value:
                st.success(msg['content'])
            else:
                st.write(msg['content'])
            
show_history()