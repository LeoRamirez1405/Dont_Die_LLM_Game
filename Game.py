from game_objects import *
from prompts import *
from API_Fireworks import * 
from history import History
from tools import *
from function_call import *
import openai
import random

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

class Game:
    def __init__(self):
<<<<<<< HEAD
        self.fc_situation_solver_attr = Function_Call(client, [Tools[fc.SITUATION_SOLVER]], fc_situation_solver)
=======
        self.destiny = random()
        self.fc_situation_solver = Function_Call(client, [Tools[fc.SITUATION_SOLVER]], fc_situation_solver)
        self.fc_valid_action = Function_Call(client, [Tools[fc.VALID_ACTION]], fc_valid_action)
        self.fc_init_player = Function_Call(client, [Tools[fc.INIT_PLAYER]], fc_init_player_)
>>>>>>> 517769fed767444e4ade42aaa41f8ab1ee3be2c0
        
        self.player = 8
        self.history = History()
        self.world = ""
        self.turn = 0
        self.turn = 0
        self.chat = API()
        self.opportunities = 3
        self.gameOver = False
        
    def possible_Action(self, situation, world, response, features) -> bool:
        return bool(post_action_appropriate(situation, world, response, features))
    
    def survive_Action(self, situation, world, response, features) -> bool:
        return bool(post_action_survive(situation, world, response, features))
         
    
    def bad_Action(self, situation, world, response, features) -> str:
        return bad_result(situation, world, response, features)

    def Play(self):

        if self.turn > 0 and (self.turn % 5) == 0: #Todo La idea de esto es ir aumentado la dificultad del juego
            pass
        self.turn += 1

        situation = self.challange_Moment(self.world, self.history, self.player.resumen_character, self.player.features()) # Situación a enfrentarse el jugador en este turno

        print(situation)

        player_action = input() # Respuesta del jugador 

        if not self.valid_Action(player_action):
            self.opportunities-=1
            if self.opportunities == 0:
                #todo implementar baneo por perdida de oportunidades
<<<<<<< HEAD
                pass

        #* Resultado de la acción (cambios de estidisticas del personaje, items, armas)
=======
                print("Has perdido")
                self.gameOver = True
                return 
        
        if not self.survive_Action(self, situation, self.world, response, self.player.features()):
            bad_answer = self.bad_Action(self, situation, self.world, response, self.player.features())
            print(bad_answer)
            self.opportunities-=1
            if self.opportunities == 0:
                #todo implementar baneo por perdida de oportunidades
                print("Has perdido")
                self.gameOver = True
                return 
            
        #* Resultado de la acción (cambios de estadisticas del personaje, items, armas)
>>>>>>> 517769fed767444e4ade42aaa41f8ab1ee3be2c0

        post_action = self.situation_Solver(situation, self.world, response, self.player.features()) # Desenlace de la situación

        new_items =  self.item_Post_Action(situation, player_action, self.player) # Nuevo item

        new_weapons =  self.item_Post_Action(situation, player_action, self.player) # Nueva arma

        if self.endGame():
            pass

        return         

    def challange_Moment(self, world, history, player, features) -> str:
        request = challenge( world, history, player, features)
        return self.chat.send_simple_request(UserType.SYSTEM.value, request)

    def situation_Solver(self, situation, world, response, player, features) -> str:
        prompt = post_action_development(situation, world, response, features)
        result = self.chat.send_simple_request(UserType.USER.value, prompt)
        
        # Function call
        self.fc_situation_solver.call(result)
        
        return result
   
    def story_Resumen(self) -> str:
        return self.history.summary()

    def valid_Action(self, situation, world, response, features) -> bool:
        possible = post_action_appropriate(situation, world, response, features)
        survives = post_action_survive(situation, world, response)
        
        return bool(survives) and bool(possible)

    def item_Post_Action(self) -> item:
        return 
        pass
    def weapon_Post_Action(self) -> weapon:
        pass
    def endGame(self) -> bool:
        pass
    
content = "You are in a dangerous situation and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"
game = Game()
game.fc_situation_solver_attr.call(content)