-
from enum import Enum
class fc(Enum):
    SITUATION_SOLVER = 0
    INIT_PLAYER = 1
    SURVIVE_ACTION = 2
    POSSIBLE_ACTION = 3

Tools = {
    fc.SITUATION_SOLVER:
        {
            "type": "function",
            "function": {
                "name": "fc_situation_solver",
                "description": "Solve a situation based on the given attributes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "strength": {
                            "type": "integer",
                            "description": "Strength attribute value."
                        },
                        "agility": {
                            "type": "integer",
                            "description": "Agility attribute value."
                        },
                        "intelligence": {
                            "type": "integer",
                            "description": "Intelligence attribute value."
                        },
                        "health": {
                            "type": "integer",
                            "description": "Health attribute value."
                        },
                        "luck": {
                            "type": "integer",
                            "description": "Luck attribute value."
                        }
                    },
                    "required": ["strength", "agility", "intelligence", "health", "luck"]
                }
            }
        },
        
    fc.INIT_PLAYER: {
         "type": "function",
         "function": {
             "name": "fc_init_player_",
             "description": "Initializes a player character with given attributes and returns a dictionary of these attributes.",
             "parameters": {
                 "type": "object",
                 "properties": {
                     "name": {
                         "type": "string",
                         "description": "The player's name."
                     },
                     "type": {
                         "type": "string",
                         "description": "The player's type."
                     },
                     "strength": {
                         "type": "integer",
                         "description": "The player's strength attribute."
                     },
                     "agility": {
                         "type": "integer",
                         "description": "The player's agility attribute."
                     },
                     "intelligence": {
                         "type": "integer",
                         "description": "The player's intelligence attribute."
                     },
                     "health": {
                         "type": "integer",
                         "description": "The player's health attribute."
                     },
                     "luck": {
                         "type": "integer",
                         "description": "The player's luck attribute."
                     }
                 },
                 "required": ["name","type","strength", "agility", "intelligence", "health", "luck"]
            },
        },
    },
    
    fc.POSSIBLE_ACTION: {
        "type": "function",
        "function": {
            "name": "fc_possible_action",
            "description": "Evaluates if the player survives according to the given situation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "possible": {
                        "type": "boolean",
                        "description": "Indicates if the action is possible."
                    },
                },
                "required": ["possible"],
            },
        },
    },
    fc.SURVIVES_ACTION: {
        "type": "function",
        "function": {
            "name": "fc_survives_action",
            "description": "Evaluates if player is survives and if the player survives based on the given situation.",
            "parameters": {
                "type": "object",
                "properties": {
                    "survives": {
                        "type": "boolean",
                        "description": "Indicates if the player survives the action."
                    }
                },
                "required": ["survives"],
            },
        },
    }
}

    


    