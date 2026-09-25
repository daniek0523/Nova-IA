import sys
from brain import NovaBrain
from actions import execute_action

# Inicializamos el cerebro de Nova
brain = NovaBrain()

def main():
    print("=========================================")
    print("        PROYECTO NOVA: EN LÍNEA          ")
    print(" Sistemas cargados. Esperando órdenes... ")
    print("=========================================")
    
    while True:
        try:
            # Tu entrada de texto en la consola
            user_input = input("\n Daniek $ ")
            
            # Comandos para apagar el sistema
            if user_input.lower() in ["salir", "exit", "apagar"]:
                print("\nDesconectando sistemas. Adiós, jefe.")
                break
                
            if not user_input.strip():
                continue
                
            print("[Pensando...]")
            
            # Nova procesa lo que dijiste con la API de Groq
            response = brain.ask(user_input)
            
            # Imprime la respuesta de Nova en pantalla
            print(f"\nNova: {response}")
            
            # Verifica y ejecuta acciones automáticas si lo pediste
            action_result = execute_action(user_input)
            if action_result:
                print(f"[SISTEMA]: {action_result}")
                
        except KeyboardInterrupt:
            print("\n\nInterrupción forzada. Apagando núcleos.")
            break

if __name__ == "__main__":
    main()