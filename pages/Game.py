import streamlit as st
from src.Game import Game
from src.prompts import *
from src.API_Fireworks import UserType
import json

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

game = Game()

try:
    with open('data/world.json', 'r') as f:
        data = json.load(f) 
        game.world = data['world']
        
    with open('data/player.json', 'r') as f:
            data = json.load(f)
            game.player = data['player']
        
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
    
    if not 'history' in st.session_state:
        st.session_state.history = []
    if not 'situation' in st.session_state:
        st.session_state.situation = ''
        
except Exception as e:
    st.warning('You need to generate the world and select a player first')
    st.error(e)
    st.stop()
    
    
    
def show_history():
    for msg in game.history:
        st.chat_message(msg['role'], msg['content'])

while not game.gameOver:
    show_history()
    
    if len(situation) > 0:
        game.turn += 1
        situation = game.challange_Moment(game.world, game.history, game.player.resumen_character, game.player.features()) # Situación a enfrentarse el jugador en este turn
        st.session_state.situation = situation
        # st.write(situation)
        
        st.session_state.hitory.append({
        'role': UserType.SYSTEM.value, 'contente': situation
        })
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'contente': '¿Cómo va actuar en esta situación?'
        })
        
        # st.chat_message(UserType.SYSTEM.value, situation)
        # st.chat_message(UserType.ASSISTANT.value, '¿Cómo va actuar en esta situación?')
        st.rerun()
        
    response = st.chat_input() 
    
    if not response:
        st.stop()
        
    st.session_state.hitory.append({
        'role': UserType.USER.value, 'contente': response
    })
        
    # game.chat(UserType.USER.value, response)
    if not game.fc_possible_action.call(post_action_appropriate(situation, game.world, response, game.features())):
        error = "Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad."
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'contente': error
        })
        st.chat_messaje(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        
        save_game_state(game)
        continue
    
    if not game.fc_survives_action.call(post_action_survive(situation, game.world, response)):
        error = "Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad."
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'contente': error
        })
        st.chat_messaje(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        
        save_game_state(game)
        continue
    
    if game.opportunities == 0:
            #todo implementar baneo por perdida de oportunidades
            print("Has perdido")
            game.gameOver = True
            save_game_state(game)
            break 
            
    #* Resultado de la acción (cambios de estadisticas del personaje, items, armas
    post_action = game.situation_Solver(situation, game.world, response, game.player.features()) # Desenlace de la situació
    print(post_action)
    st.session_state.hitory.append({'role': UserType.SYSTEM.value, 'contente': post_action})
    # st.chat_message(UserType.SYSTEM.value, post_action)
    st.session_state.situation = ''
    st.rerun()
    