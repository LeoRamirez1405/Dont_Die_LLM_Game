import google.generativeai as genai
import os

class Gemini_APi:
    def __init__(self):
            """Inicializa la clase y configura la API de Gemini"""
            os.environ['API_KEY'] = 'AIzaSyB86IMkIMmwAuXJ5sWq7bymyPAW9Ommn8c'  # Reemplaza con tu clave de API
            genai.configure(api_key=os.environ['API_KEY'])
        