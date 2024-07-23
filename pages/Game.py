import streamlit as st
from src.Game import Game
from src.game_objects import character
from src.prompts import *
from src.API_Fireworks import UserType
import json
from enum import Enum

class files(Enum):
    Player = 'player'
    Game_State = 'game_state'
    World = 'world'
    History = 'history'
    Situation = 'situation'
    Response = 'response'

def save(json_file, file):
    try:
        with open(f'data/{file}.json', 'w') as f:
            json.dump(json_file, f)
    except:
        pass

def save_game_state(game: Game):
    try:
        with open('data/game_state.json', 'w') as f:
            json.dump({
                'turn': game.turn,
                'opportunities': game.opportunities,
                'gameOver': game.gameOver
            }, f)
    except Exception as e:
        st.error(e)
        
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
    with open('data/world.json', 'r') as f:
        data = json.load(f) 
        game.world = data['world']
        
    with open('data/player.json', 'r') as f:
            data = json.load(f)
            game.player = get_palyer(data['player'])
        
    # Set game state
    try:  
        with open('data/game_state.json', 'r') as f:
            data = json.load(f)  
            game.turn = data['turn']
            game.opportunities = data['opportunities']
            game.gameOver = data['gameOver'] 
    except:
        save_game_state(game)
    
    st.success('Loaded players')
        
except Exception as e:
    st.warning('You need to generate the world and select a player first')
    st.error(e)
    st.stop()
    
try:  
    with open('data/situation.json', 'r') as f:
        data = json.load(f)  
        st.session_state.situation = data['situation']
    print('Loaded situation')
except:
    st.session_state.situation = ''
    save({'situation': ''}, files.Situation.value)
    print('Generated situation')
    
try:  
    with open('data/history.json', 'r') as f:
        data = json.load(f)  
        st.session_state.history = data['history']
    print('Loaded history')
except:
    st.session_state.history = []
    save({'history': []}, files.History.value)
    print('Generated history')    

try:  
    with open('data/response.json', 'r') as f:
        data = json.load(f)  
        st.session_state.response = data['response']
    print('Loaded response')
except:
    st.session_state.response = []
    save({'response': ''}, files.Response.value)
    print('Generated response') 
    
    
def show_history():
    for msg in st.session_state.history:
        with st.chat_message(msg['role']):
            st.write(msg['content'])

while not game.gameOver:
    show_history()
    
    if len(st.session_state.situation) == 0:
        game.turn += 1
        situation = game.challange_Moment(game.world, game.history, game.player.resumen_character, game.player.features()) # Situación a enfrentarse el jugador en este turn
        st.session_state.situation = situation
        save({'situation': situation}, files.Situation.value)
        
        st.session_state.history.append({
        'role': UserType.SYSTEM.value, 'content': situation
        })
        st.session_state.history.append({
        'role': UserType.ASSISTANT.value, 'content': '¿Cómo va actuar en esta situación?'
        })
        
        save({'history': st.session_state.history}, files.History.value)
        
        st.rerun()
        
    print('\n\n\n')
    print('Waiting for user input')
    print('\n\n\n')
    response = st.chat_input() 
    
    if not response:
        st.stop()
        
    print('\n\n\n')
    print('Received user input')
    print('\n\n\n')
    st.session_state.history.append({
        'role': UserType.USER.value, 'content': response
    })
    save({'history': st.session_state.history}, files.History.value) 
    save({'response': response}, files.Response.value)
     
    # game.chat(UserType.USER.value, response)
    if not game.fc_possible_action.call(post_action_appropriate(st.session_state.situation, game.world, response, game.player.features())):
        error = "Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad."
        
        st.session_state.history.append({
        'role': UserType.ASSISTANT.value, 'content': error
        })
        save({'history': st.session_state.history}, files.History.value)
        
        save({'response': ''}, files.Response.value)
        
        # st.chat_message(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        
        save_game_state(game)
        
        st.rerun()
        # continue
    
    if not game.fc_survives_action.call(post_action_survive(st.session_state.situation, game.world, response)):
        error = "Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad."
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'content': error
        })
        save({'history': st.session_state.history}, files.History.value)
        
        st.chat_messaje(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        
        save_game_state(game)
        continue
    
    if game.opportunities == 0:
            #todo implementar baneo por perdida de oportunidades
            print("Has perdido")
            game.gameOver = True
            save_game_state(game)
            
            st.session_state.hitory.append({
            'role': UserType.ASSISTANT.value, 'content': 'Game Over'
            })
            save({'history': st.session_state.history}, files.History.value)
            break 
            
    #* Resultado de la acción (cambios de estadisticas del personaje, items, armas
    print('\n\n\n')
    print('Processing accion')
    print('\n\n\n')
    post_action = game.situation_Solver(situation, game.world, response, game.player.features()) # Desenlace de la situació
    print('\n\n\npost_action')
    print(post_action)
    print('\n\n\n')
    
    st.session_state.history.append({'role': UserType.SYSTEM.value, 'contente': post_action})
    save({'history': st.session_state.history}, files.History.value)
  
    st.session_state.situation = ''
    save({'situation': ''}, files.Situation.value)
    
    st.rerun()
    