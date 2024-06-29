import openai
from enum import Enum

class UserType(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"
    
class API:
    def __init__(self) -> None:    
        self.client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "HAicU1zXB0SL3O8NfsRDROgkPGXzQiH7jAw9SAhObuLZvbe5"
)
     
    def send_simple_request(self,message:str,role:UserType = UserType.USER.value):
        return self.client.chat.completions.create(
            model="accounts/fireworks/models/firefunction-v2",
            messages=[{"role": role, "content": f"{message}"}],
            temperature=0.1).choices[0].message.content        

# chat = API()
# response = chat.send_simple_request(UserType.USER.value,"Hola, como puedo calcular el seno de un angulo?")
# print(response)