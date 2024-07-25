from game_objects import *
from prompts import *
from API_Fireworks import * 
# from src.API_Gemini import * 
from history import History
from tools import *
from function_call import *
import openai
# import random

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    # api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
    api_key = "wWUu45VYHt84DrkTOGIZnGu6f3DlxqPKcM4r7AVFOa6KGAZA"
)

class Game:

    FIREFUNCTION_MODEL_MAX_CONTENT = 8192
    
    def __init__(self):
        self.chat = API().send_simple_request
        self.world = self.chat(INITGAME)
        print('-'*100)
        print(self.world)
        print('-'*100)
        
        self.fc_init_player = Function_Call(client, [Tools[fc.INIT_PLAYER]], fc_init_player_)
        self.option_players = self.options() 
        self.player:character = self.initPlayer()

        self.fc_situation_solver = Function_Call(client, [Tools[fc.SITUATION_SOLVER]], fc_situation_solver)
        self.fc_survives_action = Function_Call(client, [Tools[fc.SURVIVES_ACTION]], fc_survives_action)
        self.fc_possible_action = Function_Call(client, [Tools[fc.POSSIBLE_ACTION]], fc_possible_action)
        
        self.history = History()
        self.turn = 0
        self.opportunities = 2
        self.gameOver = False
    
    def options(self):
        options = self.chat(player_init_op(self.world))
        options = eval(options)
        print(options)
        return options
        
    def initPlayer(self):
        response = self.chat(user_response_option(self.world,input()))
        init_stats = self.chat(player_init_stats(self.world, response, character.features_as_types()))
        # print(init_stats)
        result:character = self.fc_init_player.call(init_stats)
        return result
    
    def generate_world(self):
        print('WORLD')
        print('-'*100)

        self.world = self.chat(INITGAME)
        return self.world
        
    def get_players_to_select(self, world = None):
        return self.chat(player_init_op(world)) if world else self.chat(player_init_op(self.world))
    
    def select_player(self, response):
        # response = self.chat(input())
        init_stats = player_init_stats(self.world, response, character.features_as_types())
        # print(f'\n\ninit_stats\n{init_stats}')
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

            if self.opportunities == 0 or self.player.health <= 0:
                    #todo implementar baneo por perdida de oportunidades
                    print("Has perdido")
                    self.gameOver = True
                    return 
                
            situation = self.challange_Moment() # Situación a enfrentarse el jugador en este turno

            print(situation)

            response = input("¿Cómo va actuar en esta situación?:") # Respuesta del jugador 
            
            if not self.fc_possible_action.call(post_action_appropriate(situation, self.world, response, features=str(self.player))):
                print("Respuesta no válida. Tus habilidades no se corresponden a las reglas de tu mundo. Pierdes una oportunidad.")
                self.opportunities-=1
                continue

            if not self.fc_survives_action.call(post_action_survive(situation, self.world, response)):
                print("Respuesta no válida. Tus habilidades no son suficientes para superar el reto. Pierdes una oportunidad.")
                self.opportunities-=1
                continue
            
            
                
            #* Resultado de la acción (cambios de estadisticas del personaje, items, armas)

            # post_action = self.situation_Solver(situation, response) # Desenlace de la situación

            
            
            update, development = self.situation_Solver(situation, response)
            (self.player).update_skills(update)
            print("-------------------------")
            print(self.player)    
            print("-------------------------")


            self.history.increase(situation, development)
            
            token_estimate = self.history.get_token_estimate()
            if token_estimate >= Game.FIREFUNCTION_MODEL_MAX_CONTENT:
                self.history.summary()

        #loss_item = self.loss_Item_Post_Action(situation, response)
        #update_weapon = self.update_Weapons_Post_Action(situation, response)
        #loss_staistics = self.loss_Statistics_Post_Action(situation, response)
        #new_items =  self.item_Post_Action(situation, response, self.player) # Nuevo item
        #new_weapons =  self.item_Post_Action(situation, response, self.player) # Nueva arma



        #if self.endGame():
        #    pass

        return         

    def challange_Moment(self) -> str:
        request = challenge(self.world, self.history, self.player)
        return self.chat(request)

    def situation_Solver(self, situation, response) -> str:
        development = self.chat(post_action_development(situation, self.world, response))
        print("\n")
        print(development)
        result = self.fc_situation_solver.call(development)
        return result, development
   
    def story_Resumen(self) -> str:
        return self.history.summary()

    def item_Post_Action(self) -> item:
        pass

    def loss_Weapons_Post_Action(self):
        pass

    def loss_Statistics_Post_Action(self):
        pass
    
game = Game()
game.Play()
