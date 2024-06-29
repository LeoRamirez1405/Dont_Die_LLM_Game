import openai
import json

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)


tool_valid_action = [
    {
    "type": "function",
    "function": {
        "name": "fc_valid_action",
        "description": "Evaluates if an action is possible and if the player survives based on the given situation.",
        "parameters": {
            "type": "object",
            "properties": {
                "possible": {
                    "type": "boolean",
                    "description": "Indicates if the action is possible."
                },
                "survives": {
                    "type": "boolean",
                    "description": "Indicates if the player survives the action."
                }
            },
            "required": ["possible", "survives"],
        },
    },
}
]

def fc_valid_action(possible:bool, survives:bool) -> bool:
    """
    Dada la situación y la respuesta del jugador, se evalua si la acción es posible y si sobrevive.
    """
    if possible and survives:
        return True
    else:
        return False    

def valid_action(text) -> bool:
    messages = [
        {"role": "system", "content": f"You are a helpful assistant with access to functions. Use them if required."},
    
        {"role": "user", "content": text}
    ]

    chat_completion = client.chat.completions.create(
        model="accounts/fireworks/models/firefunction-v2",
        messages=messages,
        tools=tool_valid_action,
        temperature=0.1
    )
    
    print(chat_completion.choices[0].message.model_dump_json(indent=4))
    function_call = chat_completion.choices[0].message.tool_calls[0].function
    tool_response = globals()[function_call.name](**json.loads(function_call.arguments))
    print(tool_response)

valid_action("El jugador puede sobrevivir a la acción y es posible dadas las circunstancias del juego actual")