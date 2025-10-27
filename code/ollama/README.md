# Ejemplos de Código - Ollama

Esta carpeta contiene ejemplos prácticos de uso de Ollama con Llama.

## 📁 Contenido

### Ejemplos Básicos
- `simple_chat.py` - Chatbot simple en terminal
- `streaming_response.py` - Respuestas con streaming
- `model_info.py` - Información de modelos

### Ejemplos Intermedios
- `custom_personality.py` - Chatbot con personalidad personalizada
- `conversation_memory.py` - Chat con memoria de conversación
- `file_processor.py` - Procesamiento de archivos de texto

### Ejemplos Avanzados
- `api_server.py` - Servidor API con FastAPI
- `batch_processing.py` - Procesamiento en lotes
- `model_comparison.py` - Comparación de modelos

## 🚀 Comenzar

### Prerequisitos

```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelo
ollama pull llama3.2:3b

# Instalar dependencias Python
pip install -r requirements.txt
```

### Ejecutar Ejemplos

```bash
# Ejemplo básico
python simple_chat.py

# Con modelo específico
python simple_chat.py --model llama3.1:8b

# Servidor API
python api_server.py
```

## 📚 Documentación

Para más información, consulta la [documentación completa](../../docs/README.md).
