from game_objects import *
from prompts import *
from API_Fireworks import * 
import random 
class Game:
    def __init__(self):
        self.destiny = random()
        self.player
        self.history = ""
        self.world = ""
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
            

        #* Resultado de la acción (cambios de estidisticas del personaje, items, armas)

        

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
        request = post_action_development(situation, world, response, player, features)
        return self.chat.send_simple_request(UserType.USER.value, request)
        
    #def valid_Action(self, situation, world, response, features) -> bool:
    #    possible = post_action_appropriate(situation, world, response, features)
    #    survives = post_action_survive(situation, world, response)
    #    return possible

    def possible_Action(self, situation, world, response, features) -> bool:
        return bool(post_action_appropriate(situation, world, response, features))
    
    def survive_Action(self, situation, world, response, features) -> bool:
        return bool(post_action_survive(situation, world, response, features))
         
    
    def bad_Action(self, situation, world, response, features) -> str:
        return bad_result(situation, world, response, features)


    def story_Summary(self) -> str:
        return 

    def endGame(self) -> bool:
        pass

    def obtein_Item_Post_Action(self,situation, world, response, features) -> item:
        result = obtein_item_post_action(situation, world, response, features)
        return result
        
    def obtein_Weapon_Post_Action(self, situation, world, response, features) -> weapon:
        result = obtein_weapon_post_action(situation, world, response, features)
        return result
    
    def obtain_statistics_Post_Action(self, situation, world, response, features):
        result = obtein_staistics_post_action(situation, world, response, features)
        return result
    
    def loss_Item_Post_Action(self):
        pass

    def loss_Weapons_Post_Action(self):
        pass

    def loss_Statistics_Post_Action(self):
        pass


    
    
