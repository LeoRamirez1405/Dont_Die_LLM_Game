import streamlit as st
from Game import Game
from prompts import *
from API_Fireworks import UserType

try:
    game: Game = st.session_state.game
    history = st.session_state.history
    situation = st.ssesion_state.situation
except:
    game = Game()
    st.session_state.game = game
    history = st.session_state.history = []
    situation = st.session_state.situation = ''
    
st.write(game.world)

def show_history():
    for msg in game.history:
        st.chat_message(msg['role'], msg['content'])

while not game.gameOver:
    show_history()
    
    if len(situation) == 0:
        game.turn += 1
        situation = game.challange_Moment(game.world, game.history, game.player.resumen_character, game.player.features()) # Situación a enfrentarse el jugador en este turn
        st.session_states.situation = situation
        st.write(situation)
        
        st.session_state.hitory.append({
        'role': UserType.SYSTEM.value, 'contente': situation
        })
        
    st.chat_messaje(UserType.SYSTEM.value, situation)
    st.chat_messaje(UserType.ASSISTANT.value, '¿Cómo va actuar en esta situación?')
    
    response = st.chat_input() 
    
    if not response:
        st.stop()
        
    st.session_state.hitory.append({
        'role': UserType.USER.value, 'contente': response
    })
        
    game.chat(UserType.USER.value, response)
    if not game.fc_possible_action.call(post_action_appropriate(situation, game.world, response, game.features())):
        error = "Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad."
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'contente': error
        })
        st.chat_messaje(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        continue
    
    if not game.fc_survives_action.call(post_action_survive(situation, game.world, response)):
        error = "Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad."
        st.session_state.hitory.append({
        'role': UserType.ASSISTANT.value, 'contente': error
        })
        st.chat_messaje(UserType.ASSISTANT.value, error)
        game.opportunities-=1
        continue
    
    if game.opportunities == 0:
            #todo implementar baneo por perdida de oportunidades
            print("Has perdido")
            game.gameOver = True
            break 
            
    #* Resultado de la acción (cambios de estadisticas del personaje, items, armas
    post_action = game.situation_Solver(situation, game.world, response, game.player.features()) # Desenlace de la situació
    print(post_action)
    st.session_state.hitory.append({'role': UserType.SYSTEM.value, 'contente': post_action})
    st.chat_messaje(UserType.SYSTEM.value, post_action)
    st.session_state.situation = ''
    