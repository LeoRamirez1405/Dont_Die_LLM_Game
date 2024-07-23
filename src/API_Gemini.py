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
        os.environ["API_KEY"] = "AIzaSyCimaxUS5qRIB6iIw643Rr_NWvbh9ze8VU"   
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def send_simple_request(self,message:str,role:UserType = UserType.USER.value):
        response = self.model.generate_content(message)
        
        return response.text

        
# chat = API()
# response = chat.send_simple_request("Hola, como puedo calcular el seno de un angulo?",UserType.USER.value)
# print(response)