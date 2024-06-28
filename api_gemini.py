
        """Genera un mensaje a partir de los vectores de temas original y final"""

        # Formatear los vectores de temas como cadenas

        topics_str = str(topics)

        # Instrucciones para el modelo
        instructions = f"""
        Te voy a dar un vector de temas. 
        El vector representa una tupla de titulos y un numero entre -2 y 2
        
        El mensaje que generes debe de tener una longitud aproximadamente de no mas de 2 oraciones por tema. Un valor
        de -2 representa que se hable negativamente del tema, descartando su importancia, uno de 2 indica lo 
        opuesto. 0 indica neutralidad en el tema
        
        Tu trabajo es generar un nuevo mensaje en lenguaje natural que refleje 
        las opiniones y los temas del vector de temas. 


        "input: ' \"Vector de temas final: [('Environment and sustainability', -2), ('Economy and finance', 2)]\"",
        "output: \n\"Si bien la preocupación por el medio ambiente ha sido un tema en el pasado, ya no nos importa,  el enfoque principal debe estar en el crecimiento económico. La prosperidad financiera es la prioridad. Alcanzar la estabilidad económica debe ser nuestra prioridad para asegurar un futuro sólido y sostenible.\"",
        "input: \n\"Vector de temas final: [('Education and learning', -1), ('Work and career', 2)]\"",
        "output: \n\"Si bien la educación tiene su valor, la prioridad principal debe ser preparar a los estudiantes para ingresar al mercado laboral con las habilidades necesarias para tener éxito. La formación debe enfocarse en la adquisición de conocimientos prácticos y relevantes para las demandas actuales de las empresas, asegurando así su empleabilidad y competitividad en el mundo profesional.\"",
        "input: \n\"Vector de temas final: [('Technology and society', -2), ('Community and society', 2)]\"",
        "output: \n\"Aunque la tecnología nos ha prometido conexión, en realidad nos ha llevado por un camino de aislamiento y desconexión real. Es fundamental fomentar la interacción humana y la construcción de comunidades fuertes, dejando de lado la dependencia excesiva de dispositivos y plataformas digitales que, a la larga, nos alejan de lo que realmente importa: las relaciones interpersonales y el sentido de pertenencia.\"",
        "input: \n\"Vector de temas final: [('Justice and human rights', -2), ('Communication and media', 2)]\"",
        "output: \n\"Si bien se habla mucho de derechos y justicia, la realidad es que la libertad de expresión debe ser absoluta. La posibilidad de expresar cualquier opinión, incluso las que algunos consideran ofensivas, es fundamental para una sociedad abierta y democrática. Limitar la comunicación, aunque sea con la intención de proteger, puede ser un camino peligroso hacia la censura y el control.\"",
        "input:  "\n\"Vector de temas final: {topics_str}\n\",
        "output: ",
        """
        
        # Generar el mensaje
        response = self.model.generate_content(instructions)
        return response.text.strip()