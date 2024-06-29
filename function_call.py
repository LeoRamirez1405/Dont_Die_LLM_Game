import openai
import json
from openai import OpenAI

class Function_Call:
    def __init__(self, client: OpenAI, tool, func):
        self.client = client
        self.tool = tool
        self.func = func
        
    def call(self, content):
        chat_completion = self.client.chat.completions.create(
            model="accounts/fireworks/models/firefunction-v2",
            messages=[{"role": "user", "content": f"{content}"}],
            tools=self.tool,
            temperature=0.1)
        # print(chat_completion.choices[0].message.model_dump_json(indent=4))
        
        function_call = chat_completion.choices[0].message.tool_calls[0].function
        local = globals()[function_call.name](**json.loads(function_call.arguments))
        print(local)
        return local
    
def fc_situation_solver(strength, agility, intelligence, health, luck) -> dict:
    res = dict()
    res['strength'] = strength
    res['intelligence'] = intelligence
    res['agility'] = agility
    res['health'] = health
    res['luck'] = luck

    return res

content = "You are in a dangerous situation and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"
tool = [
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
    ]

func_call = FunctionCall(client, tool, content, fc_situation_solver)
func_call.call()