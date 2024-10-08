from src.API_Fireworks import UserType, API
# from src.API_Gemini import UserType, API

class History:
    def __init__(self) -> None:
        self.api = API()
        self.history = ""
        
    def get(self):
        return self.history
        
    def increase(self, challenge, development):
        self.history += f"chalenge:  {challenge} \n development: {development} \n"
        print(self.history)

    def get_token_estimate(self):
        return len(self.history.split()) * 2

    def __str__(self):
        return self.history
    
    def summary(self):
        prompt = f"""
        El texto {self.history} representa el historial de un juego. Tiene la estructura:
        >>>
            challenge: <reto al que se enfrenta el jugador>
            development: <sucesos ocurridos en el juego cuando el jugador se enfrenta al reto>
            challenge: <reto al que se enfrenta el jugador>
            development: <sucesos ocurridos en el juego cuando el jugador se enfrenta al reto>
            ...
        >>>
        
        Dame un resumen en forma de texto del este historial con un número de tokens MENOR O IGUAL que la mitad de tokens generados 
        por el historial sin resumir.Ejemplo: 
        Teniendo el historial:
            >>>
                challenge: <Te encuentras con un lobo en el bosque. El lobo hambriento comienza a asecharte provocando un enfrentamiento.>
                development: <El jugador recoge una rama del suelo y la transforma en un arma de combate. Con la lanza resultante ataca al lobo y gana
                la batalla.>
                challenge: <En la oscuridad de la noche corres por el bosque y caes por un acantilado.>
                development: <La terrible caída provoca daños casi irreparables. El jugador sufre una hemorragia interna.>
                ...
            >>>  
        un posible resumen sería:
            El jugador mata a un lobo al enfrentarse con él en el bosque. Luego cae por un acantilado y sufre una hemorragia interna.
            
        Sé consciso y elimina del resumen una instroducción similar a:
            A continuación, te presento un resumen del historial de juego en forma de texto con un número de tokens menor o igual que la mitad de tokens generados por el historial sin resumir.
        
        """
        
        return self.api.send_simple_request(UserType.USER.value, prompt) 
    
# hist = History()
# # hist.increase("Te encuentras un lobo en el bosque", "El jugador golpea al lobo con la rama de un arbol y el lobo muere")
# # hist.increase("Te caes por un acantilado", "El jugador tiene un hemorragia interna")
# hist.increase("Al entrar en una antigua mansión abandonada, te encuentras con una habitación llena de espejos. Los espejos empiezan a moverse y reflejar imágenes perturbadoras, creando una sensación de pánico.",
#     "El jugador decide romper los espejos para detener las imágenes perturbadoras. Al hacerlo, descubre un pasaje secreto detrás de uno de los espejos. Avanzas por el pasaje y encuentras una sala llena de tesoros antiguos.")
# hist.increase("Mientras exploras el tesoro, sientes un escalofrío. Una sombra oscurece la entrada de la sala. Se abre una puerta oculta revelando a un guardián de la mansión, un espíritu malévolo.",
#     "El jugador enfrenta al guardián en una batalla épica. Utiliza los objetos encontrados entre los tesoros para fortalecer sus habilidades. Después de una dura pelea, logra derrotar al espíritu y salir de la mansión con éxito.")
# #     challenge: <Al salir de la mansión, te encuentras en medio de un bosque encantador bajo el sol poniente. Sin embargo, notas algo extraño. Las flores parecen estar observándote.>
# #     development: <El jugador se da cuenta de que las flores son en realidad criaturas mágicas que hablan. Ellas le cuentan sobre un antiguo hechizo que solo puede ser desactivado si se encuentra un objeto especial en el bosque. Con la ayuda de las criaturas, el jugador logra encontrar el objeto y desactivar el hechizo, liberando así al bosque de su maleficio.>
# # print(hist.get())
# print(hist.summary())