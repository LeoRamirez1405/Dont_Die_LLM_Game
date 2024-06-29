from game_objects import *
class Game:
    def __init__(self):
        self.player
        self.turn
        self.opportunities = 3
        self.gameOver = False

    def Play(self):

        if self.turn > 0 and (self.turn % 5) == 0: #Todo La idea de esto es ir aumentado la dificultad del juego
            pass
        self.turn += 1

        turn_history = self.turn_History() # Situación a enfrentarse el jugador en este turno

        print(turn_history)

        player_action = input() # Respuesta del jugador 

        if not self.valid_Action(player_action):
            self.opportunities-=1
            if self.opportunities == 0:
                #todo implementar baneo por perdida de oportunidades
                pass

        #* Resultado de la acción (cambios de estidisticas del personaje, items, armas)

        post_action = self.situation_solver() # Desenlace de la situación 

        new_items =  self.item_Post_Action(turn_history, player_action, self.player) # Nuevo item

        new_weapons =  self.item_Post_Action(turn_history, player_action, self.player) # Nueva arma

        if self.endGame():
            pass

        return 

        

            

    def situation_solver(self) -> str:
        pass
    def story_Resumen(self) -> str:
        pass
    def valid_Action(self) -> bool:
        pass
    def item_Post_Action(self) -> item:
        pass
    def weapon_Post_Action(self) -> weapon:
        pass
    def endGame(self) -> bool:
        pass
    def turn_History(self) -> str:
        pass 
