from game_objects import *
from prompts import *
# from API_Fireworks import * 
from API_Gemini import * 
from history import History
from tools import *
from function_call import *
import openai
# import random

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

class Game:
    def __init__(self):
        self.chat = API().send_simple_request
        self.world = self.chat(INITGAME)
        print(self.world)
        print('-'*100)
        
        # self.destiny = random()
        # self.player:character = self.initPlayer()
        
        self.fc_init_player = Function_Call(client, [Tools[fc.INIT_PLAYER]], fc_init_player_)
        self.player:character = self.initPlayer()
        self.fc_situation_solver = Function_Call(client, [Tools[fc.SITUATION_SOLVER]], fc_situation_solver)
        self.fc_survives_action = Function_Call(client, [Tools[fc.SURVIVES_ACTION]], fc_survives_action)
        self.fc_possible_action = Function_Call(client, [Tools[fc.POSSIBLE_ACTION]], fc_possible_action)
        self.history = History()
        self.turn = 0
        self.opportunities = 3
        self.gameOver = False
        
    def get_players_to_select(self):
        return self.chat(player_init_op(self.world))
    
    def select_player(self, response):
        response = self.chat(input())
        init_stats = player_init_stats(self.world, response, character.features_as_types())
        print(init_stats)
        result:character = self.fc_init_player.call(init_stats)
        
        self.player = result
        return result
    
    # def possible_Action(self, situation, world, response, features) -> bool:
    #     return bool(post_action_appropriate(situation, world, response, features))
    
    # def survive_Action(self, situation, world, response, features) -> bool:
    #     return bool(post_action_survive(situation, world, response, features))
         
    
    # def bad_Action(self, situation, world, response, features) -> str:
    #     return bad_result(situation, world, response, features)

    def Play(self):

        while not self.gameOver:
            self.turn += 1

            situation = self.challange_Moment(self.world, self.history, self.player.resumen_character, self.player.features()) # Situación a enfrentarse el jugador en este turno

            print(situation)

            response = input("¿Cómo va actuar en esta situación?:") # Respuesta del jugador 
            
            self.chat(UserType.USER.value, response)
            if not self.fc_possible_action.call(post_action_appropriate(situation, self.world, response, self.features())):
                print("Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad.")
                self.opportunities-=1
                

            if not self.fc_survives_action.call(post_action_survive(situation, self.world, response)):
                print("Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad.")
                self.opportunities-=1
            
            if self.opportunities == 0:
                    #todo implementar baneo por perdida de oportunidades
                    print("Has perdido")
                    self.gameOver = True
                    return 
            #* Resultado de la acción (cambios de estadisticas del personaje, items, armas)

            post_action = self.situation_Solver(situation, self.world, response, self.player.features()) # Desenlace de la situación

            print(post_action)

        #loss_item = self.loss_Item_Post_Action(situation, response)
        #update_weapon = self.update_Weapons_Post_Action(situation, response)
        #loss_staistics = self.loss_Statistics_Post_Action(situation, response)
        #new_items =  self.item_Post_Action(situation, response, self.player) # Nuevo item
        #new_weapons =  self.item_Post_Action(situation, response, self.player) # Nueva arma



        #if self.endGame():
        #    pass

        return         

    def challange_Moment(self, world, history, player, features) -> str:
        request = challenge(world, history, player, features)
        return self.chat(request)

    def situation_Solver(self, situation, world, response, player, features) -> str:
        prompt = post_action_development(situation, world, response, features)
        result = self.chat(prompt)
        self.fc_situation_solver.call(result)
        return result
   
    def story_Resumen(self) -> str:
        return self.history.summary()

    def item_Post_Action(self) -> item:
        pass

    def loss_Weapons_Post_Action(self):
        pass

    def loss_Statistics_Post_Action(self):
        pass
    
# content = "You are in a dangerous situation and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"
# game = Game()
# game.fc_situation_solver_attr.call(content)