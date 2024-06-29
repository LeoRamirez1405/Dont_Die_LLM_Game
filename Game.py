from game_objects import *
from prompts import *
from API_Fireworks import * 
from history import History
from nlc import *

class Game:
    def __init__(self):

        self.player
        self.history = History()
        self.world = ""
        self.turn
        self.chat = API()
        self.opportunities = 3
        self.gameOver = False

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
                pass

        #* Resultado de la acción (cambios de estadisticas del personaje, items, armas)

        post_action = self.situation_Solver() # Desenlace de la situación 

        new_items =  self.item_Post_Action(situation, player_action, self.player) # Nuevo item

        new_weapons =  self.item_Post_Action(situation, player_action, self.player) # Nueva arma

        if self.endGame():
            pass

        return         

    def challange_Moment(self, world, history, player, features) -> str:
        request = challenge( world, history, player, features)
        return self.chat.send_simple_request(UserType.SYSTEM.value, request)

    def situation_Solver(self, situation, world, response, player, features) -> str:
        prompt = post_action_development(situation, world, response, player, features)
        result = self.chat.send_simple_request(UserType.USER.value, prompt)
        fc_situation_solver(result)
        return result

    def story_Resumen(self) -> str:
        return self.history.summary()

    def valid_Action(self, situation, world, response, features) -> bool:
        possible = post_action_appropriate(situation, world, response, features)
        survives = post_action_survive(situation, world, response)
        result = fc_valid_action(possible, survives)
        return result

    def item_Post_Action(self) -> item:
        return 
        pass
    def weapon_Post_Action(self) -> weapon:
        pass
    def endGame(self) -> bool:
        pass
    
