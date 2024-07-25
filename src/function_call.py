import openai
import json
from openai import OpenAI
from game_objects import character

class Function_Call:
    def __init__(self, client: OpenAI, tool, func):
        self.client = client
        self.tool = tool
        self.func = func
        
    def call(self, content):
        chat_completion = self.client.chat.completions.create(
            model="accounts/fireworks/models/firefunction-v2",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant with access to functions." 
     															"Usa una obligatoriamente."},
                {"role": "user", "content": f"{content}"}],
            tools=self.tool,
            temperature=0.1)
        
        
        # print(chat_completion.choices[0].message.model_dump_json(indent=4))
        # print('-'*200)
        # print('\n\n\nTOOL CONTENT\n\n\n')
        # print(chat_completion.choices[0].message.model_dump_json(indent=4))
        
        # print()
        # print('-'*200)
        # function_call = chat_completion.choices[0].message.tool_calls[0].function
        # function_call = chat_completion.choices
        # 
        # print(function_call)
        # print(self.tool)
        
        # print('-'*100)
        # Verificar que chat_completion y sus atributos no sean None
        # if not chat_completion or not chat_completion.choices:
        #     raise ValueError("No choices found in chat completion.")
# 
        choice = chat_completion.choices[0]
# 
        if not choice.message:
            raise ValueError("No message found in the choice.")
# 
        message = choice.message
# 
        if not message.tool_calls:
            raise ValueError("No tool calls found in the message.")
# 
        tool_call = message.tool_calls[0]
# 
        if not tool_call.function:
            raise ValueError("No function found in the tool call.")
# 
        # Si todo está bien, asignar la función
        function_call = tool_call.function
        # return function_call
        # 
        # print('-'*100)
       # 
        local = globals()[function_call.name](**json.loads(function_call.arguments))
        # print(local)
        return local
    
def fc_situation_solver(strength = 0, agility = 0, intelligence = 0, health = 0, luck = 0) -> dict:
    res = dict()
    res.setdefault('strength', 0) 
    res.setdefault('intelligence', 0) 
    res.setdefault('agility', 0) 
    res.setdefault('health', 0) 
    res.setdefault('luck', 0) 
    
    res['strength'] += strength
    res['intelligence'] += intelligence
    res['agility'] += agility
    res['health'] += health
    res['luck'] += luck

    return res

def fc_init_player_(type:str,strength:int, agility:int, intelligence:int, health:int, luck:int) -> character:
    # print(f"{strength=} {agility=} {intelligence=}")
    # res = dict()
    # # res['name'] = name
    # res['type'] = type
    # res['strength'] = strength
    # res['intelligence'] = intelligence
    # res['agility'] = agility
    # res['health'] = health
    # res['luck'] = luck
    
    player = character(type,strength,intelligence,agility,health,luck)
    return player

def fc_possible_action(possible:bool) -> bool:
    """
    Dada la situación y la respuesta del jugador, se evalua si la acción es posible y si sobrevive.
    """
    return possible

def fc_survives_action(survives:bool) -> bool:
    """
    Dada la situación y la respuesta del jugador, se evalua si la acción es posible y si sobrevive.
    """
    return survives

