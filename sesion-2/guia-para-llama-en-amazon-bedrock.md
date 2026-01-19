# Guia para Llama en Amazon Bedrock

## Acceso escalable, seguro y sin gestión de infraestructura

> Para MiPyMEs que necesitan IA en producción sin complejidad técnica

***

## Introducción

Amazon Bedrock ofrece acceso simplificado a modelos Llama (y otros) a través de una API completamente administrada. En lugar de gestionar servidores, actualizaciones y escalabilidad, Bedrock se encarga de todo —permitiéndote enfocarte en construir aplicaciones de IA. Este enfoque es ideal para:

* **MiPyMEs sin equipo DevOps** → Deploy en minutos, no semanas
* **Startups que escalan rápido** → Autoescalado automático
* **Empresas reguladas** → Cumplimiento LFPDPPP y encriptación nativa
* **Proyectos con datos sensibles** → Datos NO se usan para entrenar modelos de Bedrock
* **Equipos que prefieren APIs** → Sin gestión de contenedores, GPUs ni dependencias complejas

Diferencia clave con Local:

* ✅ **Bedrock:** Paga por uso, escalabilidad infinita, cero mantenimiento, compliance built-in
* ❌ **Local:** Compra GPU cara, gestiona actualizaciones, recursos limitados a tu máquina

***

## Requisitos Previos

### Cuenta AWS Activa

Necesitas:

* Cuenta AWS (si no tienes, crea en https://aws.amazon.com)
* Acceso a consola AWS Management
* Tarjeta de crédito para billing (aunque Bedrock tiene tier gratuito limitado)

Costo estimado (Llama 2 70B):

* Entrada: $0.00195 por 1K tokens
* Salida: $0.00256 por 1K tokens
* Ejemplo: 10,000 requests de 500 tokens cada uno ≈ $15-20/mes

### Permisos IAM

Tu usuario AWS necesita permisos Bedrock. Opción recomendada: adjunta política `AmazonBedrockFullAccess` a tu usuario.

```json
// Política mínima recomendada
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:*"
      ],
      "Resource": "*"
    }
  ]
}
```

### Habilitar Modelo Llama en Bedrock

{% stepper %}
{% step %}
### Habilitar modelos Llama en Bedrock

Pasos:

* Ve a AWS Console → Bedrock → Model Access
* Busca "Llama"
* Click "Enable" en los modelos Llama que necesites:
  * `Llama 2 Chat 7B` (rápido, económico)
  * `Llama 2 Chat 13B` (balanceado)
  * `Llama 2 Chat 70B` (más potente)
* Espera 1-2 minutos a habilitación
{% endstep %}
{% endstepper %}

### Instalar AWS SDK Python

```bash
pip install boto3
pip install aws-cli-v2  # Opcional, para CLI
```

### Configurar Credenciales AWS

Opción A (Recomendado para desarrollo):

```bash
aws configure

# Ingresa:

# AWS Access Key ID: [Tu key]

# AWS Secret Access Key: [Tu secret]

# Default region: us-east-1 (donde está Bedrock disponible)

# Default output: json
```

Opción B (Variables de entorno):

```bash
export AWS_ACCESS_KEY_ID="tu-access-key"
export AWS_SECRET_ACCESS_KEY="tu-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

Opción C (En código):

```python
import boto3

client = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    aws_access_key_id='tu-key',
    aws_secret_access_key='tu-secret'
)
```

***

## Paso 1: Invocación Básica de Llama en Bedrock

### Script Simple: Tu Primer Request

{% code title="bedrock_llama_basic.py" %}
```python
import boto3
import json

# Crear cliente Bedrock Runtime
client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Parámetros del modelo
model_id = "meta.llama2-70b-chat-v1"  # Puedes cambiar a 7b o 13b

# Tu prompt
prompt = "Explica en 50 palabras qué es Amazon Bedrock"

# Formatear input según especificaciones Llama
body = {
    "prompt": f"[INST] {prompt} [/INST]",
    "max_gen_len": 512,
    "temperature": 0.7,
    "top_p": 0.9
}

# Invocar modelo
response = client.invoke_model(
    modelId=model_id,
    body=json.dumps(body),
    contentType='application/json',
    accept='application/json'
)

# Procesar respuesta
response_body = json.loads(response['body'].read())
print("Respuesta Llama:")
print(response_body['generation'])
print("\nTokens utilizados:")
print(f"  Entrada: {response_body['prompt_token_count']}")
print(f"  Salida: {response_body['generation_token_count']}")
```
{% endcode %}

Ejecución:

```bash
python bedrock_llama_basic.py
```

Output esperado:

```
Respuesta Llama:
Amazon Bedrock es un servicio administrado que proporciona acceso a modelos de lenguaje de gran escala a través de una API. Permite a desarrolladores crear aplicaciones de IA sin gestionar infraestructura, con escalabilidad automática y seguridad nativa.

Tokens utilizados:
  Entrada: 14
  Salida: 48
```

***

## Paso 2: Conversación Multi-Turno (Chatbot)

### Script: Mantener Contexto Conversacional

{% code title="bedrock_chatbot.py" %}
```python
import boto3
import json

class LlamaBedrocktChatbot:
    def __init__(self, model_id="meta.llama2-70b-chat-v1"):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.model_id = model_id
        self.conversation_history = []
        self.total_input_tokens = 0
        self.total_output_tokens = 0
    
    def chat(self, user_message):
        """
        Envía mensaje y mantiene contexto conversacional
        """
        # Agregar mensaje usuario al historial
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Construir prompt con historial completo
        prompt = self._build_prompt()
        
        # Preparar body para Bedrock
        body = {
            "prompt": prompt,
            "max_gen_len": 1024,
            "temperature": 0.7,
            "top_p": 0.9
        }
        
        # Invocar
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType='application/json',
            accept='application/json'
        )
        
        # Parsear respuesta
        response_body = json.loads(response['body'].read())
        assistant_message = response_body['generation'].strip()
        
        # Actualizar historial
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        # Tracking de tokens
        self.total_input_tokens += response_body['prompt_token_count']
        self.total_output_tokens += response_body['generation_token_count']
        
        return assistant_message
    
    def _build_prompt(self):
        """
        Construir prompt con historial conversacional
        Formato Llama 2: [INST] ... [/INST]
        """
        prompt_parts = []
        
        for message in self.conversation_history:
            if message['role'] == 'user':
                prompt_parts.append(f"[INST] {message['content']} [/INST]")
            else:
                prompt_parts.append(f"{message['content']}")
        
        return "\n".join(prompt_parts)
    
    def get_token_usage(self):
        """Retorna estadísticas de tokens utilizados"""
        return {
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens
        }
    
    def reset_conversation(self):
        """Limpiar historial para nueva conversación"""
        self.conversation_history = []

# Uso
if __name__ == "__main__":
    chatbot = LlamaBedrocktChatbot()
    
    # Turno 1
    print("Usuario: ¿Qué es una MiPyME?")
    response1 = chatbot.chat("¿Qué es una MiPyME?")
    print(f"Llama: {response1}\n")
    
    # Turno 2 (mantiene contexto)
    print("Usuario: ¿Cómo pueden usar IA?")
    response2 = chatbot.chat("¿Cómo pueden usar IA?")
    print(f"Llama: {response2}\n")
    
    # Turno 3
    print("Usuario: Dame un ejemplo práctico")
    response3 = chatbot.chat("Dame un ejemplo práctico")
    print(f"Llama: {response3}\n")
    
    # Estadísticas
    print("=== Estadísticas de Uso ===")
    stats = chatbot.get_token_usage()
    print(f"Tokens entrada: {stats['input_tokens']}")
    print(f"Tokens salida: {stats['output_tokens']}")
    print(f"Total: {stats['total_tokens']}")
    print(f"Costo estimado: ${(stats['input_tokens'] * 0.00195 + stats['output_tokens'] * 0.00256) / 1000:.4f}")
```
{% endcode %}

Ejecución:

```bash
python bedrock_chatbot.py
```

***

## Paso 3: Personalización Avanzada (RAG con Bedrock)

### Caso de Uso: Chatbot que Responde Preguntas Sobre Tu Base Conocimiento

{% code title="bedrock_rag.py" %}
```python
import boto3
import json
from typing import List, Dict

class LlamaBedrockRAG:
    """
    Implementa RAG (Retrieval-Augmented Generation):
    1. Busca documento relevante
    2. Lo pasa a Llama para respuesta contextualizada
    """
    
    def __init__(self, model_id="meta.llama2-70b-chat-v1"):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.model_id = model_id
        
        # Base de conocimiento simulada (en producción: BD vectorial, Elasticsearch, etc)
        self.knowledge_base = {
            "normativa_ia": """
            LFPDPPP 2025: Toda MiPyME debe obtener consentimiento explícito antes 
            de procesar datos personales con IA. Encriptación AES-256 obligatoria en tránsito.
            """,
            "derechos_empleados": """
            Los empleados tienen derecho a saber cuándo IA participa en decisiones sobre ellos.
            Prohibido monitoreo biométrico 24/7 sin consentimiento.
            """,
            "implementacion": """
            Plan 30-60-90: Semana 1 (7 quick wins), Semana 2 (8-point audit),
            Semana 3 (5 políticas), Semana 4 (capacitación + go-live).
            """
        }
    
    def retrieve_context(self, query: str, top_k: int = 1) -> str:
        """
        Busca documentos relevantes en base de conocimiento
        En producción: usar embedding + vector search
        """
        # Búsqueda simple por keywords (simplificada para ejemplo)
        keywords = query.lower().split()
        scores = {}
        
        for doc_id, content in self.knowledge_base.items():
            score = sum(1 for kw in keywords if kw in content.lower())
            scores[doc_id] = score
        
        best_doc_id = max(scores, key=scores.get)
        return self.knowledge_base[best_doc_id]
    
    def generate_with_context(self, query: str) -> Dict:
        """
        RAG Pipeline:
        1. Retrieve contexto
        2. Pass a Llama
        3. Generar respuesta
        """
        # Step 1: Retrieve
        context = self.retrieve_context(query)
        
        # Step 2: Build prompt con contexto
        system_prompt = """Eres experto en normativa de IA para MiPyMEs mexicanas.
Responde basándote SOLO en el contexto proporcionado.
Si no sabes, di "No tengo información sobre esto"."""
        
        prompt = f"""[INST] {system_prompt}

Contexto:
{context}

Pregunta: {query}
[/INST]"""
        
        # Step 3: Invoke Llama
        body = {
            "prompt": prompt,
            "max_gen_len": 1024,
            "temperature": 0.5,  # Más bajo para respuestas más precisas
            "top_p": 0.9
        }
        
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=json.dumps(body),
            contentType='application/json',
            accept='application/json'
        )
        
        response_body = json.loads(response['body'].read())
        
        return {
            "question": query,
            "context_retrieved": context[:200] + "...",
            "answer": response_body['generation'].strip(),
            "tokens": {
                "input": response_body['prompt_token_count'],
                "output": response_body['generation_token_count']
            }
        }

# Uso
if __name__ == "__main__":
    rag = LlamaBedrockRAG()
    
    questions = [
        "¿Cuál es la obligación LFPDPPP?",
        "¿Qué derechos tienen los empleados?",
        "¿Cómo implemento compliance IA?"
    ]
    
    for q in questions:
        print(f"\n📋 Pregunta: {q}")
        result = rag.generate_with_context(q)
        print(f"📌 Contexto: {result['context_retrieved']}")
        print(f"✅ Respuesta: {result['answer']}")
        print(f"📊 Tokens: {result['tokens']}")
```
{% endcode %}

***

## Paso 4: Integración en Aplicaciones (API REST)

### FastAPI + Bedrock = API de IA en 30 minutos

{% code title="bedrock_api.py" %}
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import json
import logging

# Setup
app = FastAPI(
    title="Llama API con Bedrock",
    description="API REST para acceder a Llama vía Amazon Bedrock"
)

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
logger = logging.getLogger(__name__)

# Modelos Pydantic
class LlamaRequest(BaseModel):
    prompt: str
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9

class LlamaResponse(BaseModel):
    prompt: str
    response: str
    tokens_input: int
    tokens_output: int
    cost_usd: float

# Endpoints
@app.post("/invoke", response_model=LlamaResponse)
async def invoke_llama(request: LlamaRequest):
    """
    Invocar Llama directamente
    """
    try:
        body = {
            "prompt": f"[INST] {request.prompt} [/INST]",
            "max_gen_len": request.max_tokens,
            "temperature": request.temperature,
            "top_p": request.top_p
        }
        
        response = bedrock.invoke_model(
            modelId="meta.llama2-70b-chat-v1",
            body=json.dumps(body),
            contentType='application/json',
            accept='application/json'
        )
        
        result = json.loads(response['body'].read())
        
        # Calcular costo
        cost = (result['prompt_token_count'] * 0.00195 + 
                result['generation_token_count'] * 0.00256) / 1000
        
        return LlamaResponse(
            prompt=request.prompt,
            response=result['generation'].strip(),
            tokens_input=result['prompt_token_count'],
            tokens_output=result['generation_token_count'],
            cost_usd=cost
        )
        
    except Exception as e:
        logger.error(f"Error invoking Bedrock: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_available_models():
    """
    Listar modelos disponibles
    """
    return {
        "models": [
            "meta.llama2-70b-chat-v1",
            "meta.llama2-13b-chat-v1",
            "meta.llama2-7b-chat-v1"
        ],
        "default": "meta.llama2-70b-chat-v1"
    }

@app.get("/health")
async def health_check():
    """Health check"""
    return {"status": "ok", "service": "Llama-Bedrock API"}

# Ejecutar
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
{% endcode %}

Uso:

```bash
# Instalar
pip install fastapi uvicorn

# Ejecutar
python bedrock_api.py

# Test en otra terminal
curl -X POST "http://localhost:8000/invoke" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "¿Qué es IA?", "max_tokens": 256}'
```

***

## Paso 5: Monitoreo y Optimización de Costos

### Script: Dashboard de Uso Bedrock

{% code title="bedrock_monitor.py" %}
```python
import boto3
import json
from datetime import datetime, timedelta

class BedrockMonitor:
    """
    Monitor de uso y costos en Bedrock
    """
    
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
        self.pricing = {
            "input": 0.00195,   # $ por 1K tokens entrada
            "output": 0.00256   # $ por 1K tokens salida
        }
    
    def get_usage_last_7_days(self):
        """Obtener estadísticas últimos 7 días"""
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=7)
        
        try:
            response = self.cloudwatch.get_metric_statistics(
                Namespace='AWS/Bedrock',
                MetricName='InvocationTokens',
                StartTime=start_time,
                EndTime=end_time,
                Period=86400,  # 1 día
                Statistics=['Sum']
            )
            
            total_tokens = sum(dp['Sum'] for dp in response['Datapoints'])
            estimated_cost = total_tokens * self.pricing['input'] / 1000
            
            return {
                "period": "Last 7 days",
                "total_tokens": total_tokens,
                "estimated_cost": f"${estimated_cost:.2f}",
                "daily_avg": f"{total_tokens/7:.0f} tokens/day"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def optimize_recommendations(self):
        """Recomendaciones de optimización"""
        return {
            "recommendations": [
                "1. Usar Llama 2 7B para tareas simples (25% más barato)",
                "2. Cachear prompts comunes para evitar re-processing",
                "3. Implementar RAG: búsqueda precisa reduce tokens innecesarios",
                "4. Batch processing: agrupar requests para mejor throughput",
                "5. Usar temperature=0.5 para tareas determinísticas (menos varianza)"
            ]
        }

# Uso
monitor = BedrockMonitor()
print("📊 Uso Últimos 7 Días:")
print(monitor.get_usage_last_7_days())
print("\n💡 Optimizaciones:")
print(monitor.optimize_recommendations())
```
{% endcode %}

***

## Paso 6: Seguridad y Compliance para MiPyMEs

### Checklist: Protegiendo Datos en Bedrock

{% code title="security_checklist.py" %}
```python
"""
SEGURIDAD Y COMPLIANCE EN BEDROCK PARA MIPYMES MEXICANAS
"""

security_checklist = {
    "LFPDPPP": [
        "✅ Bedrock encripta datos en tránsito (TLS 1.2+)",
        "✅ Datos en reposo: encriptación con AWS KMS",
        "✅ NO utiliza datos para entrenar sus modelos base",
        "⚠️  Responsabilidad: Obtener consentimiento cliente antes pasar datos"
    ],
    
    "Acceso": [
        "✅ IAM roles: Restricción por usuario/aplicación",
        "✅ Logging completo en CloudTrail",
        "⚠️  Auditar quién accede qué",
        "⚠️  Rotación de AWS Access Keys cada 90 días"
    ],
    
    "Datos Sensibles": [
        "✅ Usar VPC endpoints (no exponer en internet)",
        "✅ Implementar data masking para PII",
        "⚠️  NO pasar información médica sin encriptar",
        "⚠️  NO pasar números de tarjeta sin hashing"
    ],
    
    "Monitoreo": [
        "✅ CloudWatch alertas por uso anómalo",
        "✅ Billing alerts si costo supera threshold",
        "⚠️  Revisar CloudTrail logs semanalmente",
        "⚠️  Audit trail completo para compliance"
    ]
}

print("=" * 60)
print("SEGURIDAD Y COMPLIANCE: Bedrock para MiPyMEs")
print("=" * 60)

for categoria, items in security_checklist.items():
    print(f"\n📋 {categoria.upper()}")
    for item in items:
        print(f"  {item}")
```
{% endcode %}

***

## Comparativa: Local vs Bedrock

| Aspecto          |                           Llama Local |                            Llama en Bedrock |
| ---------------- | ------------------------------------: | ------------------------------------------: |
| Setup Inicial    |                             2-3 horas |                                  10 minutos |
| Costo Hardware   |                    $1,000-3,000 (GPU) |                           $0 (paga por uso) |
| Escalabilidad    |                 Limitada a tu máquina |                        Infinita, automática |
| Mantenimiento    |        Actualizaciones, parches, CUDA |                         Cero (AWS gestiona) |
| Latencia         |                          Bajo (local) |                       Bajo (AWS optimizado) |
| Privacidad Datos |                         Control total |                    AWS gestiona, no entrena |
| Compliance       |                                Manual |           Built-in (LFPDPPP, PCI-DSS, SOC2) |
| Mejor para       | Prototipo, offline, máxima privacidad | Producción, escalabilidad, equipos pequeños |

***

## Próximos Pasos Recomendados

{% stepper %}
{% step %}
### Semana 1: Setup Bedrock

* Crear cuenta AWS.
* Habilitar modelos Llama.
* Ejecutar script básico.
* Entender precios.
{% endstep %}

{% step %}
### Semana 2: Chatbot Simple

* Implementar conversación multi-turno.
* Integrar en web/app.
* Pruebas con usuarios reales.
{% endstep %}

{% step %}
### Semana 3: RAG

* Conectar a base de conocimiento.
* Fine-tuning de prompts.
* Optimizar costos.
{% endstep %}

{% step %}
### Semana 4: Producción

* Implementar FastAPI/similar.
* Monitoreo con CloudWatch.
* Auditoría LFPDPPP.
{% endstep %}
{% endstepper %}

***

## Solución de Problemas Comunes

<details>

<summary>Error: "Access Denied"</summary>

Causa: Usuario IAM sin permisos Bedrock\
Solución: Adjuntar política AmazonBedrockFullAccess

</details>

<details>

<summary>Error: "Model not found"</summary>

Causa: Modelo no habilitado en Model Access\
Solución: Console AWS → Bedrock → Enable modelo

</details>

<details>

<summary>Error: "Rate limit exceeded"</summary>

Causa: Demasiados requests simultáneos\
Solución: Implementar backoff exponencial, usar batch APIs

</details>

<details>

<summary>Costo Muy Alto</summary>

Causa: Prompts muy largos, muchas iteraciones\
Solución: Implementar caching, usar Llama 7B, optimizar prompts

</details>

***

## Conclusión

Amazon Bedrock elimina la complejidad de ejecutar Llama en producción. Para MiPyMEs mexicanas, representa:

* ✅ Acceso inmediato a modelos SOTA sin inversión hardware
* ✅ Escalabilidad automática para crecer sin límite
* ✅ Compliance nativo para LFPDPPP y regulaciones
* ✅ Costo predecible (paga solo lo que usas)
* ✅ Equipos pequeños pueden construir grandes cosas

Comienza hoy: Sigue el Script Básico → Chatbot → RAG → Producción. En 4 semanas, tendrás sistema IA robusto y listo para escalar.

***

**Referencias:**

* **AWS Bedrock Docs:** [https://docs.aws.amazon.com/bedrock/](https://docs.aws.amazon.com/bedrock/)
* **Llama 2 Model Card:** [https://llama.meta.com/](https://llama.meta.com/)
* **Pricing Calculator:** [https://calculator.aws/](https://calculator.aws/)
