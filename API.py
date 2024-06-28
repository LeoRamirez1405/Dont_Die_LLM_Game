import google.generativeai as genai
import os

class Gemini_APi:
    def __init__(self):
            """Inicializa la clase y configura la API de Gemini"""
            os.environ['API_KEY'] = "AIzaSyAmJMgn4TofXhoMAuojBYoATYyjTSKxheo"  # Reemplaza con tu clave de API
            genai.configure(api_key=os.environ['API_KEY'])
            self.model = genai.GenerativeModel("gemini-pro")
    
    def history(self, text: str):
        response = self.model.generate_content(text)
        print(response.text)

A = Gemini_APi()
A.history("Hola")