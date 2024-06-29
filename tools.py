
from enum import Enum
class fc(Enum):
    SITUATION_SOLVER = 0

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
        }
}
