# Capítulo 4: Casos de Uso Avanzados

## 📖 Contenido

1. [Fine-Tuning de Modelos](#fine-tuning-de-modelos)
2. [Agentes con LangChain](#agentes-con-langchain)
3. [Despliegue en Producción](#despliegue-en-producción)
4. [Monitoreo y Observabilidad](#monitoreo-y-observabilidad)
5. [Optimización Avanzada](#optimización-avanzada)

---

## Fine-Tuning de Modelos

### ¿Cuándo Hacer Fine-Tuning?

- Dominio específico (legal, médico, financiero)
- Tono o estilo particular de respuestas
- Vocabulario especializado
- Formatos de salida específicos

### Preparación de Datos

```python
# prepare_dataset.py
import json

# Formato para fine-tuning de Llama
def preparar_datos_finetune(ejemplos):
    """
    ejemplos: Lista de tuplas (prompt, respuesta)
    """
    dataset = []
    
    for prompt, respuesta in ejemplos:
        # Formato JSONL para entrenamiento
        item = {
            "text": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n{respuesta}<|eot_id|>"
        }
        dataset.append(item)
    
    return dataset

# Ejemplo de dataset
ejemplos = [
    ("¿Qué es un contrato de arrendamiento?", 
     "Un contrato de arrendamiento es un acuerdo legal entre un arrendador y un arrendatario..."),
    ("Explica qué es el ISR en México",
     "El ISR (Impuesto Sobre la Renta) es un impuesto federal en México que grava los ingresos...")
]

dataset = preparar_datos_finetune(ejemplos)

# Guardar dataset
with open('dataset_finetune.jsonl', 'w', encoding='utf-8') as f:
    for item in dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
```

### Creación de Modelfile

```dockerfile
# Modelfile
FROM llama3.1:8b

# Temperatura para respuestas más consistentes
PARAMETER temperature 0.5

# Número de predicciones de contexto
PARAMETER num_ctx 4096

# System prompt personalizado
SYSTEM """
Eres un experto en derecho corporativo mexicano.
Proporciona respuestas precisas, citando artículos cuando sea posible.
Usa un tono profesional pero accesible.
"""

# Agregar datos de fine-tuning (opcional)
# ADAPTER ./path/to/adapter
```

### Crear Modelo Personalizado

```bash
# Crear modelo desde Modelfile
ollama create abogado-mx -f Modelfile

# Probar el modelo
ollama run abogado-mx "¿Qué es una sociedad anónima?"

# Listar modelos
ollama list
```

## Agentes con LangChain

### Agente con Herramientas

```python
# agent_tools.py
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.llms import Ollama
from langchain import hub
import requests
import datetime

# Inicializar LLM
llm = Ollama(model="llama3.1:8b")

# Definir herramientas
def obtener_clima(ciudad: str) -> str:
    """Obtiene el clima de una ciudad (simulado)"""
    # En producción, conectar a API real como OpenWeatherMap
    return f"El clima en {ciudad} es soleado con 25°C"

def calcular_expresion(expresion: str) -> str:
    """Calcula una expresión matemática"""
    try:
        resultado = eval(expresion)
        return f"El resultado es: {resultado}"
    except:
        return "No pude calcular esa expresión"

def obtener_fecha() -> str:
    """Obtiene la fecha actual"""
    return datetime.datetime.now().strftime("%d de %B de %Y")

# Crear herramientas
tools = [
    Tool(
        name="Clima",
        func=obtener_clima,
        description="Útil para obtener información del clima. Input: nombre de ciudad"
    ),
    Tool(
        name="Calculadora",
        func=calcular_expresion,
        description="Útil para hacer cálculos matemáticos. Input: expresión matemática"
    ),
    Tool(
        name="Fecha",
        func=obtener_fecha,
        description="Útil para obtener la fecha actual. No requiere input"
    )
]

# Crear agente
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Usar agente
if __name__ == "__main__":
    resultado = agent_executor.invoke({
        "input": "¿Qué día es hoy y cuál es el clima en Monterrey?"
    })
    print(resultado['output'])
```

### Cadena de Procesamiento RAG

```python
# advanced_rag.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class AdvancedRAG:
    def __init__(self, model_name="llama3.1:8b"):
        self.llm = Ollama(model=model_name)
        self.embeddings = OllamaEmbeddings(model=model_name)
        self.vectorstore = None
        
    def cargar_documentos(self, textos):
        """Carga y procesa documentos"""
        # Dividir texto en chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        chunks = text_splitter.create_documents(textos)
        
        # Crear vectorstore
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            collection_name="knowledge_base"
        )
        
    def crear_cadena_qa(self):
        """Crea cadena de preguntas y respuestas"""
        # Template personalizado
        template = """Usa el siguiente contexto para responder la pregunta.
        Si no sabes la respuesta, di que no lo sabes, no inventes información.
        
        Contexto: {context}
        
        Pregunta: {question}
        
        Respuesta útil en español:"""
        
        QA_CHAIN_PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )
        
        # Crear cadena QA
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 3}
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )
        
        return qa_chain
    
    def responder(self, pregunta):
        """Responde pregunta con fuentes"""
        qa_chain = self.crear_cadena_qa()
        resultado = qa_chain({"query": pregunta})
        
        return {
            "respuesta": resultado["result"],
            "fuentes": resultado["source_documents"]
        }

# Ejemplo de uso
if __name__ == "__main__":
    rag = AdvancedRAG()
    
    # Cargar documentos
    documentos = [
        "Llama 3.1 es la última versión del modelo de Meta AI.",
        "Ollama permite ejecutar modelos localmente sin necesidad de GPUs.",
        "El fine-tuning adapta modelos a casos de uso específicos.",
    ]
    
    rag.cargar_documentos(documentos)
    
    # Hacer pregunta
    resultado = rag.responder("¿Qué es Ollama?")
    print(f"Respuesta: {resultado['respuesta']}")
    print(f"\nFuentes: {len(resultado['fuentes'])} documentos")
```

## Despliegue en Producción

### Dockerización

```dockerfile
# Dockerfile
FROM python:3.11-slim

# Instalar Ollama
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puertos
EXPOSE 8000
EXPOSE 11434

# Script de inicio
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
```

```bash
# start.sh
#!/bin/bash

# Iniciar Ollama en background
ollama serve &

# Esperar a que Ollama esté listo
sleep 5

# Descargar modelo si no existe
ollama pull llama3.1:8b

# Iniciar aplicación
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - llama_network
    
  api:
    build: .
    container_name: llama_api
    ports:
      - "8000:8000"
    depends_on:
      - ollama
    environment:
      - OLLAMA_HOST=http://ollama:11434
    networks:
      - llama_network
    
  nginx:
    image: nginx:alpine
    container_name: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./html:/usr/share/nginx/html
    depends_on:
      - api
    networks:
      - llama_network

volumes:
  ollama_data:

networks:
  llama_network:
    driver: bridge
```

### Configuración Nginx

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream api_backend {
        server api:8000;
    }
    
    server {
        listen 80;
        server_name localhost;
        
        # Frontend
        location / {
            root /usr/share/nginx/html;
            index index.html;
            try_files $uri $uri/ /index.html;
        }
        
        # API Proxy
        location /api/ {
            proxy_pass http://api_backend/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            
            # Timeouts para LLM
            proxy_read_timeout 300s;
            proxy_connect_timeout 300s;
        }
    }
}
```

## Monitoreo y Observabilidad

### Logging Estructurado

```python
# logger_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
        }
        
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        
        return json.dumps(log_data)

def setup_logging():
    logger = logging.getLogger('llama_app')
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    
    return logger

# Uso
logger = setup_logging()
logger.info('Iniciando aplicación', extra={'model': 'llama3.1:8b'})
```

### Métricas con Prometheus

```python
# metrics.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Definir métricas
requests_total = Counter(
    'llama_requests_total',
    'Total de requests a Llama',
    ['model', 'status']
)

request_duration = Histogram(
    'llama_request_duration_seconds',
    'Duración de requests',
    ['model']
)

active_requests = Gauge(
    'llama_active_requests',
    'Requests activos',
    ['model']
)

def track_request(model='llama3.1:8b'):
    """Decorator para trackear requests"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            active_requests.labels(model=model).inc()
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                requests_total.labels(model=model, status='success').inc()
                return result
            except Exception as e:
                requests_total.labels(model=model, status='error').inc()
                raise e
            finally:
                duration = time.time() - start_time
                request_duration.labels(model=model).observe(duration)
                active_requests.labels(model=model).dec()
        
        return wrapper
    return decorator

# Uso en FastAPI
from fastapi import FastAPI
from prometheus_client import make_asgi_app

app = FastAPI()

# Montar endpoint de métricas
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.post("/chat")
@track_request(model="llama3.1:8b")
async def chat(request):
    # Tu lógica aquí
    pass
```

## Optimización Avanzada

### Batch Processing

```python
# batch_processor.py
import asyncio
from typing import List
import ollama

class BatchProcessor:
    def __init__(self, model="llama3.1:8b", max_workers=4):
        self.model = model
        self.max_workers = max_workers
    
    async def process_single(self, prompt):
        """Procesa un prompt"""
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: ollama.generate(model=self.model, prompt=prompt)
        )
        return response['response']
    
    async def process_batch(self, prompts: List[str]):
        """Procesa múltiples prompts en paralelo"""
        semaphore = asyncio.Semaphore(self.max_workers)
        
        async def bounded_process(prompt):
            async with semaphore:
                return await self.process_single(prompt)
        
        tasks = [bounded_process(prompt) for prompt in prompts]
        results = await asyncio.gather(*tasks)
        return results

# Uso
async def main():
    processor = BatchProcessor()
    
    prompts = [
        "Resume el capítulo 1 de Don Quijote",
        "¿Cuál es la capital de México?",
        "Explica qué es la fotosíntesis"
    ]
    
    results = await processor.process_batch(prompts)
    
    for prompt, result in zip(prompts, results):
        print(f"Prompt: {prompt}")
        print(f"Resultado: {result[:100]}...\n")

if __name__ == "__main__":
    asyncio.run(main())
```

### Caché Inteligente con Redis

```python
# redis_cache.py
import redis
import json
import hashlib
import ollama

class LlamaCache:
    def __init__(self, redis_host='localhost', redis_port=6379):
        self.redis_client = redis.Redis(
            host=redis_host,
            port=redis_port,
            decode_responses=True
        )
        self.ttl = 3600  # 1 hora
    
    def _generate_key(self, prompt, model):
        """Genera key única para prompt y modelo"""
        content = f"{model}:{prompt}"
        return f"llama:{hashlib.sha256(content.encode()).hexdigest()}"
    
    def get(self, prompt, model):
        """Obtiene respuesta del caché"""
        key = self._generate_key(prompt, model)
        cached = self.redis_client.get(key)
        
        if cached:
            return json.loads(cached)
        return None
    
    def set(self, prompt, model, response):
        """Guarda respuesta en caché"""
        key = self._generate_key(prompt, model)
        self.redis_client.setex(
            key,
            self.ttl,
            json.dumps(response)
        )
    
    def generate_with_cache(self, prompt, model="llama3.1:8b"):
        """Genera con caché"""
        # Intentar obtener del caché
        cached = self.get(prompt, model)
        if cached:
            print("✓ Respuesta desde caché")
            return cached
        
        # Generar nueva respuesta
        print("⟳ Generando nueva respuesta")
        response = ollama.generate(model=model, prompt=prompt)
        result = response['response']
        
        # Guardar en caché
        self.set(prompt, model, result)
        
        return result

# Uso
cache = LlamaCache()
respuesta = cache.generate_with_cache("¿Qué es Python?")
```

## 🎯 Proyecto Final

Crea un sistema completo que incluya:

1. **API REST** con FastAPI
2. **Sistema RAG** con ChromaDB
3. **Caché** con Redis
4. **Métricas** con Prometheus
5. **Logging** estructurado
6. **Dockerización** completa
7. **Frontend** funcional

## 📚 Recursos Avanzados

- [LangChain Documentation](https://python.langchain.com/)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

## ➡️ Siguiente Paso

Consulta los [Anexos](./anexos.md) para información adicional y recursos.
