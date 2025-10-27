# Glosario de Términos

## 📚 Terminología de IA y LLMs

### A

**Agent (Agente)**
Sistema de IA que puede tomar decisiones y realizar acciones de manera autónoma, utilizando herramientas y planificación para alcanzar objetivos.

**API (Application Programming Interface)**
Interfaz que permite la comunicación entre diferentes aplicaciones de software. En el contexto de Llama, se refiere a cómo interactuar con el modelo programáticamente.

**Attention Mechanism (Mecanismo de Atención)**
Componente clave de los Transformers que permite al modelo enfocarse en partes relevantes del input al generar output.

### B

**Batch Processing (Procesamiento por Lotes)**
Técnica de procesar múltiples entradas simultáneamente para mejorar eficiencia.

**BPTT (Back-Propagation Through Time)**
Algoritmo de entrenamiento para redes neuronales recurrentes.

### C

**Checkpoint**
Estado guardado de un modelo durante el entrenamiento, permite reanudar o usar el modelo desde ese punto.

**ChromaDB**
Base de datos vectorial especializada en almacenar y buscar embeddings para sistemas RAG.

**Context Length (Longitud de Contexto)**
Cantidad máxima de tokens que un modelo puede procesar simultáneamente. Llama 3.1 soporta hasta 128k tokens.

**Context Window (Ventana de Contexto)**
Porción del texto que el modelo puede "ver" al mismo tiempo para generar respuestas.

**Cuantización (Quantization)**
Proceso de reducir la precisión numérica de los pesos del modelo para disminuir tamaño y aumentar velocidad.
- **Q8**: 8 bits - alta calidad
- **Q4**: 4 bits - equilibrio
- **Q2**: 2 bits - máxima compresión

### D

**Decoder-Only Architecture**
Arquitectura de Transformer que solo usa el componente decoder. Llama utiliza esta arquitectura.

**Deployment (Despliegue)**
Proceso de poner un modelo de IA en producción para uso real.

**Docker**
Plataforma de contenedorización que permite empaquetar aplicaciones con sus dependencias.

### E

**Embedding**
Representación vectorial de texto que captura significado semántico. Palabras similares tienen embeddings similares.

**Epoch**
Una pasada completa por todo el dataset de entrenamiento.

**Evaluation (Evaluación)**
Proceso de medir el rendimiento de un modelo usando métricas específicas.

### F

**FastAPI**
Framework moderno de Python para crear APIs web de alto rendimiento.

**Few-Shot Learning**
Técnica donde se proporcionan pocos ejemplos al modelo para guiar sus respuestas.

**Fine-Tuning**
Proceso de entrenar un modelo preentrenado con datos específicos para adaptarlo a un caso de uso particular.

**FP16 (16-bit Floating Point)**
Formato numérico de 16 bits usado en deep learning, balance entre precisión y memoria.

### G

**GGUF (GPT-Generated Unified Format)**
Formato de archivo para modelos de lenguaje optimizado para inferencia eficiente.

**GPU (Graphics Processing Unit)**
Procesador especializado en cálculos paralelos, ideal para ejecutar modelos de IA.

**Gradient**
Derivada que indica la dirección para actualizar los pesos del modelo durante entrenamiento.

### H

**Hallucination (Alucinación)**
Cuando un LLM genera información incorrecta o inventada que parece plausible.

**Hugging Face**
Plataforma y comunidad para compartir modelos, datasets y herramientas de IA.

**Hyperparameter (Hiperparámetro)**
Configuración externa al modelo que afecta el entrenamiento o inferencia (ej: temperature, learning rate).

### I

**Inference (Inferencia)**
Proceso de usar un modelo entrenado para hacer predicciones o generar outputs.

**Instruction Tuning**
Fine-tuning específico para que el modelo siga instrucciones mejor.

### K

**Knowledge Base (Base de Conocimiento)**
Colección de información estructurada o no estructurada usada por sistemas RAG.

### L

**LangChain**
Framework para desarrollar aplicaciones con LLMs, facilita cadenas de procesamiento y agentes.

**Latency (Latencia)**
Tiempo que tarda el modelo en responder a una solicitud.

**LLM (Large Language Model)**
Modelo de lenguaje grande entrenado en vastas cantidades de texto. Ejemplo: Llama 3.1.

**LoRA (Low-Rank Adaptation)**
Técnica eficiente de fine-tuning que modifica solo una pequeña parte del modelo.

### M

**Memory (Memoria)**
En contexto de chatbots, el historial de conversación que se mantiene para coherencia.

**Mixtral**
Modelo tipo Mixture of Experts con múltiples sub-modelos especializados.

**Model Card**
Documento que describe un modelo de IA: arquitectura, capacidades, limitaciones y uso ético.

**Modelfile**
Archivo de configuración de Ollama que define parámetros y comportamiento de un modelo.

### N

**Natural Language Processing (NLP)**
Campo de IA enfocado en la interacción entre computadoras y lenguaje humano.

**Neural Network (Red Neuronal)**
Sistema de aprendizaje automático inspirado en el cerebro humano.

**Normalization (Normalización)**
Técnica para estabilizar y acelerar el entrenamiento de redes neuronales.

### O

**Ollama**
Herramienta para ejecutar LLMs localmente de forma sencilla.

**One-Shot Learning**
Técnica donde se proporciona un solo ejemplo al modelo.

**Overfitting**
Cuando un modelo aprende demasiado de los datos de entrenamiento y pierde capacidad de generalización.

### P

**Parameter (Parámetro)**
Valor aprendido durante el entrenamiento del modelo. Llama 3.1 8B tiene 8 mil millones de parámetros.

**Perplexity**
Métrica que mide qué tan "sorprendido" está el modelo con el texto. Menor perplexity = mejor.

**Prompt**
Texto de entrada que se proporciona a un LLM para generar una respuesta.

**Prompt Engineering**
Arte y ciencia de diseñar prompts efectivos para obtener mejores resultados.

### Q

**Quantization** → Ver Cuantización

**Query**
Pregunta o búsqueda realizada a un sistema, especialmente en contexto de RAG.

### R

**RAG (Retrieval-Augmented Generation)**
Técnica que combina búsqueda de información con generación de texto para respuestas más precisas.

**RLHF (Reinforcement Learning from Human Feedback)**
Técnica de entrenamiento usando feedback humano para alinear el modelo con preferencias humanas.

**RoPE (Rotary Position Embedding)**
Método de encoding posicional usado en Llama para manejar secuencias largas.

### S

**Sampling**
Proceso de seleccionar el siguiente token durante la generación de texto.

**Semantic Search (Búsqueda Semántica)**
Búsqueda basada en significado, no solo palabras clave.

**Streaming**
Envío de respuestas del modelo token por token en tiempo real.

**System Prompt**
Instrucción inicial que define el comportamiento y personalidad del asistente.

### T

**Temperature**
Parámetro que controla aleatoriedad en la generación:
- Baja (0.1-0.3): Respuestas más deterministas
- Alta (0.8-1.5): Respuestas más creativas

**Token**
Unidad básica de texto procesada por el modelo (palabra, subpalabra o carácter).

**Tokenization (Tokenización)**
Proceso de convertir texto en tokens.

**Top-K Sampling**
Técnica de sampling que considera solo los K tokens más probables.

**Top-P (Nucleus Sampling)**
Técnica de sampling que considera tokens hasta alcanzar probabilidad acumulada P.

**Transfer Learning**
Uso de conocimiento de un modelo preentrenado para una tarea relacionada.

**Transformer**
Arquitectura de red neuronal basada en atención, base de modelos como Llama.

### U

**Underfitting**
Cuando un modelo es demasiado simple y no captura patrones en los datos.

**Upstream/Downstream Tasks**
Upstream: Tareas de preentrenamiento. Downstream: Tareas específicas posteriores.

### V

**Vector Database (Base de Datos Vectorial)**
Base de datos optimizada para almacenar y buscar embeddings. Ejemplo: ChromaDB.

**Vector Embedding** → Ver Embedding

**Vision-Language Model (VLM)**
Modelo que procesa tanto imágenes como texto.

### W

**Weight (Peso)**
Valor numérico en la red neuronal que se ajusta durante el entrenamiento.

**Workflow**
Secuencia de pasos en un proceso de IA/ML.

### Z

**Zero-Shot Learning**
Capacidad del modelo de realizar tareas sin ejemplos previos de esa tarea específica.

---

## 📊 Acrónimos Comunes

| Acrónimo | Significado | Descripción |
|----------|-------------|-------------|
| AI | Artificial Intelligence | Inteligencia Artificial |
| API | Application Programming Interface | Interfaz de programación |
| BERT | Bidirectional Encoder Representations from Transformers | Modelo de lenguaje bidireccional |
| CLI | Command Line Interface | Interfaz de línea de comandos |
| CPU | Central Processing Unit | Procesador central |
| DL | Deep Learning | Aprendizaje profundo |
| GPU | Graphics Processing Unit | Unidad de procesamiento gráfico |
| GUI | Graphical User Interface | Interfaz gráfica de usuario |
| LLM | Large Language Model | Modelo de lenguaje grande |
| ML | Machine Learning | Aprendizaje automático |
| NLP | Natural Language Processing | Procesamiento de lenguaje natural |
| QA | Question Answering | Sistema de preguntas y respuestas |
| RAG | Retrieval-Augmented Generation | Generación aumentada por recuperación |
| RLHF | Reinforcement Learning from Human Feedback | Aprendizaje por refuerzo con feedback humano |
| SFT | Supervised Fine-Tuning | Fine-tuning supervisado |
| VRAM | Video RAM | Memoria de video (GPU) |

---

## 🔢 Unidades y Medidas

**Parámetros:**
- 1B = 1 mil millones (billion) de parámetros
- 1M = 1 millón de parámetros
- 1K = 1 mil parámetros

**Memoria:**
- 1 TB = 1024 GB
- 1 GB = 1024 MB
- 1 MB = 1024 KB

**Tokens:**
- ~1 token ≈ 0.75 palabras en inglés
- ~1 token ≈ 0.5-1 palabra en español
- 1000 tokens ≈ 750 palabras

**Contexto:**
- 4K tokens ≈ 3 páginas de texto
- 8K tokens ≈ 6 páginas de texto
- 128K tokens ≈ 96 páginas de texto

---

## 📖 Recursos Adicionales

Para términos más específicos o técnicos, consulta:

- [Papers With Code Glossary](https://paperswithcode.com/)
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/)
- [Google ML Glossary](https://developers.google.com/machine-learning/glossary)

---

## ⬅️ Volver

Regresa a [README principal](./README.md) o revisa los [Anexos](./anexos.md).
