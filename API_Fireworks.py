import openai
from enum import Enum
import google.generativeai as genai
import os

class UserType(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"
    
class API:
    def __init__(self) -> None:    
        self.client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key = "DA4O3HbHkhzLPA1nC7uZ4WAyCavRTTYNJxs0iWVxvosDxK2A"
    )
     
    def send_simple_request(self,message:str,role:UserType = UserType.USER.value):
        return self.client.chat.completions.create(
            model="accounts/fireworks/models/firefunction-v2",
            messages=[{"role": role, "content": f"{message}"}],
            temperature=0.1).choices[0].message.content        
        
# class API:
#     def __init__(self) -> None: 
#         os.environ["API_KEY"] = "AIzaSyCimaxUS5qRIB6iIw643Rr_NWvbh9ze8VU"   
#         genai.configure(api_key=os.environ["API_KEY"])
#         self.model = genai.GenerativeModel('gemini-1.5-flash')
        
#     def send_simple_request(self,message:str,role:UserType = UserType.USER.value):
#         response = self.model.generate_content(message)
        
#         return response.text

        
# chat = API()
# response = chat.send_simple_request(UserType.USER.value,"Hola, como puedo calcular el seno de un angulo?")
# print(response)