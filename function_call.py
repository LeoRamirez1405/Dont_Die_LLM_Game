import openai
import json
from openai import OpenAI

class FunctionCall:
    def __init__(self, client: OpenAI, tool, content, func):
        self.client = client
        self.tool = tool
        self.content = content
        self.func = func
        
    def call(self):
        chat_completion = self.client.chat.completions.create(
            model="accounts/fireworks/models/firefunction-v2",
            messages=[{"role": "user", "content": f"{self.content}"}],
            tools=self.tool,
            temperature=0.1)
        # print(chat_completion.choices[0].message.model_dump_json(indent=4))
        
        function_call = chat_completion.choices[0].message.tool_calls[0].function
        local = locals()[function_call.name](**json.loads(function_call.arguments))
        print(local)
        return local
    
    
    
client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

def fc_situation_solver(content):
    tool = [
        {
            "type": "function",
            "function": {
                "name": "fc_situation_solver_",
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
    
    chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/firefunction-v2",
    messages=[{"role": "user", "content": f"{content}"}],
    tools=tool,
    temperature=0.1)
    # print(chat_completion.choices[0].message.model_dump_json(indent=4))
    
    function_call = chat_completion.choices[0].message.tool_calls[0].function
    local = globals()[function_call.name](**json.loads(function_call.arguments))
    print(local)
    return local

def fc_situation_solver_(strength, agility, intelligence, health, luck) -> dict:
    # print(f"{strength=} {agility=} {intelligence=}")
    res = dict()
    res['strength'] = strength
    res['intelligence'] = intelligence
    res['agility'] = agility
    res['health'] = health
    res['luck'] = luck
  
    return res

content = "You are in a dangerous situation and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"
print(fc_situation_solver(content))
# fc_situation_solver(content)


tool = [
        {
            "type": "function",
            "function": {
                "name": "func",
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

#func_call = FunctionCall(client, tool, content, fc_situation_solver_)
#func_call.call()