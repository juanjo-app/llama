#!/usr/bin/env python3
"""
Chatbot simple usando Ollama y Llama
Ejemplo básico de interacción con LLM
"""

import ollama
import sys


def main():
    """
    Chatbot interactivo simple
    """
    print("🤖 Chatbot Simple con Llama")
    print("Escribe 'salir' para terminar\n")
    
    # Configuración del modelo
    model = "llama3.2:3b"
    
    # Verificar que el modelo está disponible
    try:
        ollama.show(model)
    except Exception as e:
        print(f"❌ Error: Modelo '{model}' no encontrado.")
        print(f"Descárgalo con: ollama pull {model}")
        sys.exit(1)
    
    # Historial de conversación
    conversation = []
    
    print("✓ Modelo cargado. ¡Comencemos!\n")
    
    while True:
        # Obtener entrada del usuario
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta luego!")
            break
        
        # Verificar si el usuario quiere salir
        if user_input.lower() in ['salir', 'exit', 'quit', 'q']:
            print("¡Hasta luego!")
            break
        
        # Ignorar entradas vacías
        if not user_input:
            continue
        
        # Agregar mensaje del usuario al historial
        conversation.append({
            'role': 'user',
            'content': user_input
        })
        
        # Generar respuesta
        try:
            print("🤖 Asistente: ", end='', flush=True)
            
            response = ollama.chat(
                model=model,
                messages=conversation
            )
            
            # Extraer contenido de la respuesta
            assistant_message = response['message']['content']
            
            # Mostrar respuesta
            print(assistant_message)
            print()
            
            # Agregar respuesta al historial
            conversation.append({
                'role': 'assistant',
                'content': assistant_message
            })
            
        except Exception as e:
            print(f"\n❌ Error al generar respuesta: {e}")
            # Remover el último mensaje del usuario si hubo error
            conversation.pop()


if __name__ == "__main__":
    main()
