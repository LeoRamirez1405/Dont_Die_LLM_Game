import openai
import json
from openai import OpenAI
from game_objects import character
client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)

def fc_init_player(content):
    tool = [
             {
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
]
    
    chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/firefunction-v2",
    messages=[{"role": "user", "content": f"{content}"}],
    tools=tool,
    temperature=0.1)
    # print(chat_completion.choices[0].message.model_dump_json(indent=4))
    
    function_call = chat_completion.choices[0].message.tool_calls[0].function
    local = globals()[function_call.name](**json.loads(function_call.arguments))
    character_ = character(name=local['name'],type=local['type'],strength=local['strength'], agelity=local['agility'],intelligence= local['intelligence'], health=local['health'],luck= local['luck'])
    return character_

def fc_init_player_(name:str,type:str,strength:int, agility:int, intelligence:int, health:int, luck:int) -> dict:
    # print(f"{strength=} {agility=} {intelligence=}")
    res = dict()
    res['name'] = name
    res['type'] = type
    res['strength'] = strength
    res['intelligence'] = intelligence
    res['agility'] = agility
    res['health'] = health
    res['luck'] = luck
  
    return res

content = "Inicializa al jugaddor. You are Dohaerisin the alchemist and your atributes are: strength: 0, agility: 1, intelligence: 0, health: 1, luck: 0"

print(fc_init_player(content))