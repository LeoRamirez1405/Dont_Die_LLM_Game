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
        
def save_game_state(game: Game):
    try:
        with open('data/game_state.json', 'w') as f:
            json.dump({
                'turn': game.turn,
                'opportunities': game.opportunities,
                'gameOver': game.gameOver,
                'history': game.history.history
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
            game.history.history = data['history']
    except:
        save_game_state(game)
    
    # st.success('Loaded player')
    # player_info = f"""
    # Jugador: \n\n
    # Tipo: {game.player.type} \n
    # Fuerza: {game.player.strength} \n
    # Inteligencia: {game.player.intelligence} \n
    # Agilidad: {game.player.agility} \n
    # Salud: {game.player.health} \n
    # Suerte: {game.player.luck} \n
    # # {game.player.features()}
    # """
    # st.write(player_info)
          
except Exception as e:
    st.warning('You need to generate the world and select a player first')
    st.error(e)
    st.stop()
    
try:  
    with open('data/situation.json', 'r') as f:
        data = json.load(f)  
        st.session_state.situation = data['situation']
    # print('Loaded situation')
except:
    st.session_state.situation = ''
    save({'situation': ''}, files.Situation.value)
    # print('Generated situation')
    
try:  
    with open('data/history.json', 'r') as f:
        data = json.load(f)  
        st.session_state.history = data['history']
    # print('Loaded history')
except:
    st.session_state.history = []
    save({'history': st.session_state.history}, files.History.value)
    # print('Generated history')    

try:  
    with open('data/response.json', 'r') as f:
        data = json.load(f)  
        st.session_state.response = data['response']
    # print('Loaded response')
except:
    st.session_state.response = ''
    save({'response': ''}, files.Response.value)
    # print('Generated response') 
    
    
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
            
def situation_error(error):
    st.session_state.history.append({
    'role': UserType.ASSISTANT.value, 'content': error, 'state': state_msg.error.value
    })
    
    save({'history': st.session_state.history}, files.History.value)
    save({'response': ''}, files.Response.value)
    
    game.opportunities-=1
    save_game_state(game)
    
    st.rerun()
    
def update_palyer(player: character):
     save({
        "player": {
        "type": player.type,
        "strength": player.strength,
        "intelligence": player.intelligence,
        "agility": player.agility,
        "health": player.health,
        "luck": player.luck}
    }, 'player')

while not game.gameOver:
    show_history()
    
    if len(st.session_state.situation) == 0:
        game.turn += 1
        situation = game.challange_Moment() # Situación a enfrentarse el jugador en este turn
        st.session_state.situation = situation
        save({'situation': situation}, files.Situation.value)
        
        st.session_state.history.append({
        'role': UserType.SYSTEM.value, 'content': situation, 'state': state_msg.none.value
        })
        print('History 1: ', st.session_state.history)
        st.session_state.history.append({
        'role': UserType.ASSISTANT.value, 'content': '¿Cómo va actuar en esta situación?', 'state': state_msg.none.value
        })
        print('History 2: ', st.session_state.history)
        
        save({'history': st.session_state.history}, files.History.value)
        save_game_state(game)
        
        print('Situacion generada')
        
        st.rerun()
        
    # response = st.chat_input() 
    
    with open("data/response.json", 'r') as f:
        res = json.load(f)["response"]
        if len(res) > 0:
            response = res 
        else:
            response = st.chat_input() 
            if not response:
                st.stop()

            st.session_state.history.append({
                'role': UserType.USER.value, 'content': response, 'state': state_msg.none.value
            })
            save({'history': st.session_state.history}, files.History.value) 
            save({'response': response}, files.Response.value)
     
    if not game.fc_possible_action.call(post_action_appropriate(st.session_state.situation, game.world, response, game.player.features())):
        error = "Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad."
        situation_error(error)
    
    if not game.fc_survives_action.call(post_action_survive(st.session_state.situation, game.world, response)):
        error = "Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad."
        situation_error(error)
    
    if game.opportunities == 0:
            #todo implementar baneo por perdida de oportunidades
            print("Has perdido")
            game.gameOver = True
            save_game_state(game)
            
            st.session_state.history.append({
            'role': UserType.ASSISTANT.value, 'content': 'Game Over', 'state': state_msg.warning.value
            })
            save({'history': st.session_state.history}, files.History.value)
            
            st.rerun()
            # break 
            
    update, development = game.situation_Solver(st.session_state.situation, response)
    (game.player).update_skills(update)
    update_palyer(game.player)
    
    st.session_state.situation = ''
    save({'situation': ''}, files.Situation.value)
    
    st.session_state.response = ''
    save({'response': ''}, files.Response.value)
    
    game.history.increase(st.session_state.situation, development)
    
    player_info = f"""
        **Jugador: \n
        *Tipo: {game.player.type},
        *🦾Fuerza: {game.player.strength},
        *🧠 Inteligencia: {game.player.intelligence}, 
        *🏃‍♀️Agilidad: {game.player.agility},
        *💊Salud: {game.player.health},
        *🍀Suerte: {game.player.luck}
        """
        
    st.session_state.history.append({'role': UserType.ASSISTANT.value, 'content': development + "\n " + player_info + f"\n*❤ Oportunidades: {game.opportunities}", 'state': state_msg.success.value})
    save({'history': st.session_state.history}, files.History.value)
    
    token_estimate = game.history.get_token_estimate()
    if token_estimate >= Game.FIREFUNCTION_MODEL_MAX_CONTENT:
        game.history.summary()
        
    save_game_state(game)
        
    st.rerun()


    