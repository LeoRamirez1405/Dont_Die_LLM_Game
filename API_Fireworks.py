import requests
from enum import Enum

class UserType(Enum):
    USER = "user"
    SYSTEM = "system"

class ChatDontDie:
    def __init__(self) -> None:    
        self.url = "https://api.fireworks.ai/inference/v1/chat/completions"

    def send_simple_request(self,role:UserType,message:str):
        payload = {
            "messages": [
                {
                    "content": message,
                    "role": role,
                }
            ],
            "model": "accounts/fireworks/models/llama-v3-70b-instruct",
            "response_format": {"type": "text"}
        }
        headers = {
            "Authorization": "Bearer HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5",
            "Content-Type": "application/json"
        }
        return ((requests.request("POST", self.url, json=payload, headers=headers).json()['choices'])[0])['message']['content']


chat = ChatDontDie()
response = chat.send_simple_request(UserType.USER.value,"Hola, como puedo calcular el seno de un angulo?")
print(response)