#!/usr/bin/env python3
"""
Chatbot con streaming de respuestas
Muestra la respuesta token por token en tiempo real
"""

import ollama
import sys


def stream_chat(model="llama3.2:3b"):
    """
    Chatbot con streaming de respuestas
    """
    print("🤖 Chatbot con Streaming")
    print("Escribe 'salir' para terminar\n")
    
    conversation = []
    
    while True:
        # Obtener entrada
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta luego!")
            break
        
        if user_input.lower() in ['salir', 'exit', 'quit', 'q']:
            print("¡Hasta luego!")
            break
        
        if not user_input:
            continue
        
        # Agregar mensaje del usuario
        conversation.append({
            'role': 'user',
            'content': user_input
        })
        
        print("🤖 Asistente: ", end='', flush=True)
        
        try:
            # Streaming de respuesta
            full_response = ""
            
            stream = ollama.chat(
                model=model,
                messages=conversation,
                stream=True
            )
            
            # Mostrar cada chunk a medida que llega
            for chunk in stream:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                full_response += content
            
            print("\n")
            
            # Agregar respuesta completa al historial
            conversation.append({
                'role': 'assistant',
                'content': full_response
            })
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            conversation.pop()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Chatbot con streaming")
    parser.add_argument(
        "--model",
        default="llama3.2:3b",
        help="Modelo a usar (default: llama3.2:3b)"
    )
    
    args = parser.parse_args()
    stream_chat(args.model)
