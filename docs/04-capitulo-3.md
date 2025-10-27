# Capítulo 3: Construcción de Aplicaciones

## 📖 Contenido

1. [Tu Primer Chatbot](#tu-primer-chatbot)
2. [Aplicación Web con FastAPI](#aplicación-web-con-fastapi)
3. [Sistema de Memoria](#sistema-de-memoria)
4. [Procesamiento de Archivos](#procesamiento-de-archivos)
5. [Mejores Prácticas](#mejores-prácticas)

---

## Tu Primer Chatbot

### Chatbot Simple en CLI

```python
# chatbot_simple.py
import ollama

def chatbot():
    print("🤖 Chatbot con Llama - Escribe 'salir' para terminar\n")
    
    conversacion = []
    
    while True:
        # Obtener entrada del usuario
        user_input = input("Tú: ")
        
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta luego!")
            break
        
        # Agregar mensaje del usuario
        conversacion.append({
            'role': 'user',
            'content': user_input
        })
        
        # Obtener respuesta del modelo
        response = ollama.chat(
            model='llama3.2:3b',
            messages=conversacion
        )
        
        # Agregar respuesta a la conversación
        assistant_message = response['message']['content']
        conversacion.append({
            'role': 'assistant',
            'content': assistant_message
        })
        
        print(f"\n🤖 Asistente: {assistant_message}\n")

if __name__ == "__main__":
    chatbot()
```

### Chatbot con Sistema de Personalidad

```python
# chatbot_personalizado.py
import ollama

PERSONALIDADES = {
    'amigable': "Eres un asistente amigable y entusiasta. Usas emojis ocasionalmente.",
    'profesional': "Eres un consultor profesional de negocios. Eres formal y preciso.",
    'educativo': "Eres un tutor paciente. Explicas conceptos de forma clara y pedagógica.",
    'creativo': "Eres un escritor creativo. Tus respuestas son imaginativas y artísticas."
}

def chatbot_personalizado(personalidad='amigable'):
    system_prompt = PERSONALIDADES.get(personalidad, PERSONALIDADES['amigable'])
    
    print(f"🤖 Chatbot ({personalidad}) - Escribe 'salir' para terminar\n")
    
    conversacion = [
        {'role': 'system', 'content': system_prompt}
    ]
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta luego!")
            break
        
        conversacion.append({'role': 'user', 'content': user_input})
        
        response = ollama.chat(
            model='llama3.1:8b',
            messages=conversacion
        )
        
        assistant_message = response['message']['content']
        conversacion.append({'role': 'assistant', 'content': assistant_message})
        
        print(f"\n🤖 Asistente: {assistant_message}\n")

if __name__ == "__main__":
    # Cambia la personalidad aquí
    chatbot_personalizado('educativo')
```

## Aplicación Web con FastAPI

### Backend API

```python
# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import ollama
import uvicorn

app = FastAPI(title="Llama API", version="1.0.0")

# Modelos de datos
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "llama3.1:8b"
    temperature: float = 0.7
    max_tokens: Optional[int] = None

class ChatResponse(BaseModel):
    message: str
    model: str

# Almacenamiento temporal de conversaciones
conversations = {}

@app.get("/")
async def root():
    return {
        "message": "API de Llama funcionando",
        "docs": "/docs",
        "modelos_disponibles": "/models"
    }

@app.get("/models")
async def list_models():
    """Lista modelos disponibles en Ollama"""
    try:
        models = ollama.list()
        return {"models": [model['name'] for model in models['models']]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Endpoint principal de chat"""
    try:
        # Convertir mensajes a formato Ollama
        messages = [msg.dict() for msg in request.messages]
        
        # Generar respuesta
        response = ollama.chat(
            model=request.model,
            messages=messages,
            options={
                'temperature': request.temperature,
            }
        )
        
        return ChatResponse(
            message=response['message']['content'],
            model=request.model
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate(
    prompt: str,
    model: str = "llama3.1:8b",
    temperature: float = 0.7
):
    """Generación simple de texto"""
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            options={'temperature': temperature}
        )
        
        return {
            "prompt": prompt,
            "response": response['response'],
            "model": model
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Frontend HTML Simple

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat con Llama</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .chat-container {
            width: 90%;
            max-width: 800px;
            height: 600px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
        }
        
        .chat-header {
            background: #667eea;
            color: white;
            padding: 20px;
            border-radius: 12px 12px 0 0;
        }
        
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #f7f7f7;
        }
        
        .message {
            margin-bottom: 15px;
            display: flex;
            flex-direction: column;
        }
        
        .message.user {
            align-items: flex-end;
        }
        
        .message.assistant {
            align-items: flex-start;
        }
        
        .message-content {
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 18px;
            word-wrap: break-word;
        }
        
        .message.user .message-content {
            background: #667eea;
            color: white;
        }
        
        .message.assistant .message-content {
            background: white;
            color: #333;
            border: 1px solid #e0e0e0;
        }
        
        .chat-input-container {
            padding: 20px;
            background: white;
            border-radius: 0 0 12px 12px;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 10px;
        }
        
        #messageInput {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid #e0e0e0;
            border-radius: 24px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.3s;
        }
        
        #messageInput:focus {
            border-color: #667eea;
        }
        
        #sendButton {
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 24px;
            cursor: pointer;
            font-weight: 600;
            transition: background 0.3s;
        }
        
        #sendButton:hover {
            background: #5568d3;
        }
        
        #sendButton:disabled {
            background: #ccc;
            cursor: not-allowed;
        }
        
        .typing-indicator {
            display: none;
            padding: 12px 16px;
            background: white;
            border-radius: 18px;
            border: 1px solid #e0e0e0;
            max-width: 70px;
        }
        
        .typing-indicator span {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #667eea;
            margin: 0 2px;
            animation: typing 1.4s infinite;
        }
        
        .typing-indicator span:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-indicator span:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typing {
            0%, 60%, 100% {
                transform: translateY(0);
            }
            30% {
                transform: translateY(-10px);
            }
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>🤖 Chat con Llama</h2>
            <p style="opacity: 0.9; font-size: 14px; margin-top: 5px;">Powered by Llama 3.1</p>
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message assistant">
                <div class="message-content">
                    ¡Hola! Soy tu asistente con Llama. ¿En qué puedo ayudarte hoy?
                </div>
            </div>
        </div>
        
        <div class="chat-input-container">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Escribe tu mensaje..."
                onkeypress="handleKeyPress(event)"
            >
            <button id="sendButton" onclick="sendMessage()">Enviar</button>
        </div>
    </div>

    <script>
        const messages = [];
        
        function addMessage(role, content) {
            messages.push({ role, content });
            
            const chatMessages = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${role}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function showTypingIndicator() {
            const chatMessages = document.getElementById('chatMessages');
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message assistant';
            typingDiv.id = 'typingIndicator';
            
            const indicatorDiv = document.createElement('div');
            indicatorDiv.className = 'typing-indicator';
            indicatorDiv.style.display = 'block';
            indicatorDiv.innerHTML = '<span></span><span></span><span></span>';
            
            typingDiv.appendChild(indicatorDiv);
            chatMessages.appendChild(typingDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function hideTypingIndicator() {
            const indicator = document.getElementById('typingIndicator');
            if (indicator) {
                indicator.remove();
            }
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const sendButton = document.getElementById('sendButton');
            const userMessage = input.value.trim();
            
            if (!userMessage) return;
            
            // Deshabilitar input
            input.disabled = true;
            sendButton.disabled = true;
            
            // Agregar mensaje del usuario
            addMessage('user', userMessage);
            input.value = '';
            
            // Mostrar indicador de escritura
            showTypingIndicator();
            
            try {
                // Llamar a la API
                const response = await fetch('http://localhost:8000/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        messages: messages,
                        model: 'llama3.1:8b',
                        temperature: 0.7
                    })
                });
                
                if (!response.ok) {
                    throw new Error('Error en la API');
                }
                
                const data = await response.json();
                
                // Ocultar indicador
                hideTypingIndicator();
                
                // Agregar respuesta del asistente
                addMessage('assistant', data.message);
                
            } catch (error) {
                hideTypingIndicator();
                addMessage('assistant', 'Lo siento, hubo un error al procesar tu mensaje.');
                console.error('Error:', error);
            }
            
            // Rehabilitar input
            input.disabled = false;
            sendButton.disabled = false;
            input.focus();
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
    </script>
</body>
</html>
```

## Sistema de Memoria

### Implementación con ChromaDB

```python
# rag_system.py
import chromadb
from chromadb.utils import embedding_functions
import ollama

class RAGSystem:
    def __init__(self, collection_name="knowledge_base"):
        # Inicializar ChromaDB
        self.client = chromadb.Client()
        
        # Función de embedding
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
        
        # Crear o obtener colección
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )
    
    def add_documents(self, documents, metadatas=None, ids=None):
        """Agregar documentos a la base de conocimiento"""
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(documents))]
        
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def query(self, question, n_results=3):
        """Buscar documentos relevantes"""
        results = self.collection.query(
            query_texts=[question],
            n_results=n_results
        )
        return results['documents'][0]
    
    def chat_with_context(self, question, model="llama3.1:8b"):
        """Chat con contexto de documentos relevantes"""
        # Obtener contexto relevante
        relevant_docs = self.query(question)
        context = "\n\n".join(relevant_docs)
        
        # Construir prompt con contexto
        prompt = f"""Contexto:
{context}

Pregunta: {question}

Por favor responde basándote en el contexto proporcionado. Si la información no está en el contexto, indícalo."""
        
        # Generar respuesta
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        
        return response['response']

# Ejemplo de uso
if __name__ == "__main__":
    rag = RAGSystem()
    
    # Agregar documentos
    documents = [
        "Llama es un modelo de lenguaje grande desarrollado por Meta AI.",
        "Ollama es una herramienta para ejecutar LLMs localmente en tu computadora.",
        "RAG significa Retrieval-Augmented Generation, una técnica para mejorar respuestas con información externa.",
    ]
    
    rag.add_documents(documents)
    
    # Hacer pregunta
    respuesta = rag.chat_with_context("¿Qué es Ollama?")
    print(respuesta)
```

## Procesamiento de Archivos

```python
# document_processor.py
import ollama
from pathlib import Path

def procesar_archivo_texto(archivo_path, tarea="resumir"):
    """Procesa archivos de texto con Llama"""
    
    # Leer archivo
    with open(archivo_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Plantillas de tareas
    plantillas = {
        'resumir': f"Resume el siguiente texto en español:\n\n{contenido}",
        'puntos_clave': f"Extrae los puntos clave del siguiente texto:\n\n{contenido}",
        'preguntas': f"Genera 5 preguntas sobre el siguiente texto:\n\n{contenido}",
        'traducir': f"Traduce el siguiente texto al inglés:\n\n{contenido}"
    }
    
    prompt = plantillas.get(tarea, plantillas['resumir'])
    
    # Generar respuesta
    response = ollama.generate(
        model='llama3.1:8b',
        prompt=prompt
    )
    
    return response['response']

# Ejemplo de uso
if __name__ == "__main__":
    resultado = procesar_archivo_texto('documento.txt', tarea='resumir')
    print(resultado)
```

## Mejores Prácticas

### 1. Gestión de Errores

```python
import ollama
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def safe_chat(messages, model="llama3.1:8b", max_retries=3):
    """Chat con reintentos y manejo de errores"""
    for attempt in range(max_retries):
        try:
            response = ollama.chat(model=model, messages=messages)
            return response['message']['content']
        
        except Exception as e:
            logger.error(f"Intento {attempt + 1} falló: {e}")
            if attempt == max_retries - 1:
                return "Lo siento, no pude procesar tu solicitud."
```

### 2. Caché de Respuestas

```python
import hashlib
import json
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_generate(prompt, model="llama3.1:8b"):
    """Genera respuesta con caché"""
    response = ollama.generate(model=model, prompt=prompt)
    return response['response']
```

### 3. Streaming de Respuestas

```python
def stream_chat(messages, model="llama3.1:8b"):
    """Chat con streaming para respuestas largas"""
    stream = ollama.chat(
        model=model,
        messages=messages,
        stream=True
    )
    
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print()  # Nueva línea al final
```

## 🎯 Ejercicio Práctico

1. **Crea un Chatbot Personalizado**:
   - Implementa una personalidad única
   - Agrega comandos especiales (/ayuda, /reset)
   - Guarda el historial

2. **API Web**:
   - Despliega la API de FastAPI
   - Prueba todos los endpoints
   - Crea un frontend personalizado

3. **Sistema RAG**:
   - Carga documentos sobre un tema específico
   - Crea un sistema de Q&A
   - Compara respuestas con y sin contexto

---

## 📚 Recursos

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Ollama Python Library](https://github.com/ollama/ollama-python)

## ➡️ Siguiente Paso

Avanza al [Capítulo 4: Casos de Uso Avanzados](./05-capitulo-4.md) para aprender técnicas avanzadas.
