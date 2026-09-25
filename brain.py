import groq  # Módulo para hablar con Groq
from config import GROQ_API_KEY

class NovaBrain:
    def __init__(self):
        # Conectamos con Groq usando tu llave
        self.client = groq.Client(api_key=GROQ_API_KEY)
        
        # Le damos la actitud Stark / J.A.R.V.I.S.
        self.system_prompt = (
            "Eres Nova, una inteligencia artificial avanzada, sarcástica, inteligente y muy leal. "
            "Tu personalidad está inspirada en J.A.R.V.I.S. de Iron Man. Te diriges al usuario como 'jefe'. "
            "Tu creador real es Daniek (Daniel), un joven estudiante de 14 años apasionado por la tecnología, "
            "la programación en Python y la ciberseguridad. No inventes que es un adulto ni que usa tecnologías antiguas; "
            "él es un desarrollador joven en su laboratorio actual. Mantén tus respuestas concisas, "
            "divertidas y con estilo de ciencia ficción."
        )
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        # Usamos el modelo rápido de llama 3
        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=self.messages
        )
        
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})
        return response