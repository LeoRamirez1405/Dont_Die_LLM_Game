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
    def __init__(self, type: str , strength: int , intelligence: int , agelity: int , health: int, luck: int):
        # self.name = name
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
    
    def update_skills(self,dict):
        print(dict)
        self.strength += dict['strength']
        self.intelligence += dict['intelligence']
        self.agility += dict['agility']
        self.health += dict['health']
        self.luck += dict['luck']
        
    def features(self):
        return f"Type: {self.type}\nStrength: {self.strength}\nIntelligence: {self.intelligence}\nAgility: {self.agility}\nHealth: {self.health}\nLuck: {self.luck}"
    def __str__(self):
        # Formateando la salida como una cadena que muestra todos los campos
        return f"Character Info:\nType: {self.type}\nStrength: {self.strength}\nIntelligence: {self.intelligence}\nAgility: {self.agility}\nHealth: {self.health}\nLuck: {self.luck}"
    @staticmethod
    def features_as_types():
        return f"Type: \nStrength: \nIntelligence: \nAgility: \nHealth: \nLuck:"




    

