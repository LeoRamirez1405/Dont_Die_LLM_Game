from game_objects import *
from prompts import *
from API_Fireworks import * 
from history import History
from tools import *
from function_call import *
import openai

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

class Game:
    def __init__(self):
        self.destiny = random()
        self.fc_situation_solver_attr = Function_Call(client, [Tools[fc.SITUATION_SOLVER]], fc_situation_solver)
        
        self.player = 8
        self.history = History()
        self.world = ""
        self.turn = 0
        self.turn = 0
        self.chat = API()
        self.opportunities = 3
        self.gameOver = False

    def Play(self):

        if self.turn > 0 and (self.turn % 5) == 0: #Todo La idea de esto es ir aumentado la dificultad del juego
            pass
        self.turn += 1

        situation = self.challange_Moment(self.world, self.history, self.player.resumen_character, self.player.features()) # Situación a enfrentarse el jugador en este turno

        print(situation)

        response = input("¿Cómo va actuar en esta situación?") # Respuesta del jugador 

        if not self.possible_Action(self, situation, self.world, response, self.player.features()):
            bad_answer = self.bad_Action(self, situation, self.world, response, self.player.features())
            print(bad_answer)
            self.opportunities-=1
            if self.opportunities == 0:
                #todo implementar baneo por perdida de oportunidades
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

        post_action = self.situation_Solver() # Desenlace de la situación 

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
        request = challenge( world, history, player, features)
        return self.chat.send_simple_request(UserType.SYSTEM.value, request)

    def situation_Solver(self, situation, world, response, player, features) -> str:
        prompt = post_action_development(situation, world, response, player, features)
        result = self.chat.send_simple_request(UserType.USER.value, prompt)
        
        # Function call
        self.fc_situation_solver_attr.call(result)
        
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

    def loss_Weapons_Post_Action(self):
        pass

    def loss_Statistics_Post_Action(self):
        pass
    
content = "You are in a dangerous situation and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"
game = Game()
game.fc_situation_solver_attr.call(content)