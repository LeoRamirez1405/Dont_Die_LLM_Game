class item:
    def __init__(self, name: str, description: str, pow: int):
        self.name = name
        self.description = description
        self.pow = pow
    
    def __str__(self):
        # Formateando la salida como una cadena que muestra todos los campos
        return f"Item Info:\nName: {self.name}\nDescription: {self.description}\nPower: {self.pow}"


class weapon(item):
    def __init__(self, name: str, description: str, pow: int):
        super.__init__(name, description, pow)

class character():
    def __init__(self, name: str, type: int , strength: int , intelligence: int , agelity: int , health: int, luck: int):
        self.name = name
        self.type = type
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agelity
        self.health = health
        self.luck = luck

    def state_character(self, update_state: str) -> str:
        self.body_state = update_state
    
    def resumen_character(self, update_state: str) -> str:
        self.resumen_character = update_state
    
    def __str__(self):
        # Formateando la salida como una cadena que muestra todos los campos
        return f"Character Info:\nName: {self.name}\nType: {self.type}\nStrength: {self.strength}\nIntelligence: {self.intelligence}\nAgility: {self.agility}\nHealth: {self.health}\nLuck: {self.luck}"





    

