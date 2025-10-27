#!/usr/bin/env python3
"""
Script para obtener información sobre modelos disponibles en Ollama
"""

import ollama
import json


def list_models():
    """Lista todos los modelos instalados"""
    print("📋 Modelos Instalados\n")
    
    try:
        models = ollama.list()
        
        if not models or 'models' not in models:
            print("No hay modelos instalados.")
            print("Instala uno con: ollama pull llama3.2:3b")
            return
        
        for model in models['models']:
            name = model.get('name', 'Unknown')
            size = model.get('size', 0) / (1024**3)  # Convert to GB
            modified = model.get('modified_at', 'Unknown')
            
            print(f"• {name}")
            print(f"  Tamaño: {size:.2f} GB")
            print(f"  Modificado: {modified}")
            print()
            
    except Exception as e:
        print(f"❌ Error al listar modelos: {e}")


def show_model_info(model_name):
    """Muestra información detallada de un modelo"""
    print(f"📊 Información de {model_name}\n")
    
    try:
        info = ollama.show(model_name)
        
        # Información básica
        print("=== Detalles del Modelo ===")
        
        if 'modelfile' in info:
            print(f"\nModelfile:\n{info['modelfile']}\n")
        
        if 'parameters' in info:
            print("Parámetros:")
            print(info['parameters'])
            print()
        
        if 'template' in info:
            print(f"Template:\n{info['template']}\n")
        
        # Mostrar JSON completo si se desea más detalle
        # print("\nJSON Completo:")
        # print(json.dumps(info, indent=2))
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"El modelo '{model_name}' podría no estar instalado.")
        print(f"Instálalo con: ollama pull {model_name}")


def test_model(model_name, prompt="Hola, ¿cómo estás?"):
    """Prueba rápida de un modelo"""
    print(f"🧪 Probando {model_name}\n")
    print(f"Prompt: {prompt}\n")
    
    try:
        response = ollama.generate(
            model=model_name,
            prompt=prompt
        )
        
        print("Respuesta:")
        print(response['response'])
        print()
        
        # Estadísticas
        if 'total_duration' in response:
            total_time = response['total_duration'] / 1e9  # Convert to seconds
            print(f"⏱️  Tiempo total: {total_time:.2f}s")
        
        if 'eval_count' in response and 'eval_duration' in response:
            tokens = response['eval_count']
            duration = response['eval_duration'] / 1e9
            tokens_per_sec = tokens / duration if duration > 0 else 0
            print(f"⚡ Tokens generados: {tokens} ({tokens_per_sec:.2f} tokens/s)")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Información sobre modelos de Ollama"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Listar todos los modelos"
    )
    parser.add_argument(
        "--info",
        metavar="MODEL",
        help="Mostrar información detallada de un modelo"
    )
    parser.add_argument(
        "--test",
        metavar="MODEL",
        help="Probar un modelo con un prompt simple"
    )
    parser.add_argument(
        "--prompt",
        default="Hola, ¿cómo estás?",
        help="Prompt para usar con --test"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_models()
    elif args.info:
        show_model_info(args.info)
    elif args.test:
        test_model(args.test, args.prompt)
    else:
        # Por defecto, listar modelos
        parser.print_help()
        print("\n")
        list_models()


if __name__ == "__main__":
    main()
