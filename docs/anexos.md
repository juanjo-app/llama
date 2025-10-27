# Anexos

## 📖 Contenido

1. [Comandos Útiles de Ollama](#comandos-útiles-de-ollama)
2. [Comparativa de Modelos](#comparativa-de-modelos)
3. [Recursos de Aprendizaje](#recursos-de-aprendizaje)
4. [Comunidades y Foros](#comunidades-y-foros)
5. [Datasets Públicos](#datasets-públicos)
6. [Troubleshooting Avanzado](#troubleshooting-avanzado)

---

## Comandos Útiles de Ollama

### Gestión de Modelos

```bash
# Listar modelos instalados
ollama list

# Mostrar información de un modelo
ollama show llama3.1:8b

# Ver modelo con más detalles
ollama show llama3.1:8b --modelfile

# Eliminar modelo
ollama rm llama3.1:8b

# Copiar modelo
ollama cp llama3.1:8b mi-modelo-custom
```

### Ejecución y Testing

```bash
# Ejecutar modelo interactivamente
ollama run llama3.1:8b

# Ejecutar con prompt directo
ollama run llama3.1:8b "Explica qué es la IA"

# Modo multilinea
ollama run llama3.1:8b """
Este es un prompt
de múltiples líneas
"""

# Con parámetros personalizados
ollama run llama3.1:8b \
  --temperature 0.9 \
  --top-k 50 \
  "Escribe un poema"
```

### API y Desarrollo

```bash
# Iniciar servidor
ollama serve

# Especificar puerto
OLLAMA_HOST=0.0.0.0:11434 ollama serve

# Ver logs
journalctl -u ollama -f  # Linux con systemd

# Reiniciar servicio
systemctl restart ollama  # Linux
```

### Importación y Exportación

```bash
# Crear modelo desde Modelfile
ollama create mi-modelo -f ./Modelfile

# Exportar modelo
ollama push usuario/modelo

# Importar modelo
ollama pull usuario/modelo
```

## Comparativa de Modelos

### Modelos Llama

| Modelo | Parámetros | RAM Mín. | Velocidad | Calidad | Uso Recomendado |
|--------|-----------|----------|-----------|---------|-----------------|
| Llama 3.2 1B | 1B | 2GB | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | Móvil, Edge |
| Llama 3.2 3B | 3B | 4GB | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | Chat ligero |
| Llama 3.1 8B | 8B | 8GB | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | Propósito general |
| Llama 3.1 70B | 70B | 48GB | ⚡⚡ | ⭐⭐⭐⭐⭐⭐ | Tareas complejas |
| Llama 3.1 405B | 405B | 256GB | ⚡ | ⭐⭐⭐⭐⭐⭐⭐ | Estado del arte |

### Otros Modelos en Ollama

| Modelo | Especialidad | Tamaño | Idioma |
|--------|-------------|--------|--------|
| Mistral | Propósito general | 7B | Multilingüe |
| Mixtral | Mixture of Experts | 8x7B | Multilingüe |
| CodeLlama | Programación | 7B-34B | Código |
| Phi-3 | Eficiente | 3.8B | Inglés |
| Gemma | Google | 2B-7B | Multilingüe |

### Comparativa de Cuantización

```
Modelo: Llama 3.1 8B

FP16 (Full Precision):
- Tamaño: ~16GB
- RAM necesaria: ~18GB
- Calidad: 100%
- Velocidad: Base

Q8_0:
- Tamaño: ~8.5GB
- RAM necesaria: ~10GB
- Calidad: ~99%
- Velocidad: +20%

Q5_K_M:
- Tamaño: ~5.3GB
- RAM necesaria: ~7GB
- Calidad: ~97%
- Velocidad: +40%

Q4_K_M:
- Tamaño: ~4.7GB
- RAM necesaria: ~6GB
- Calidad: ~95%
- Velocidad: +60%

Q2_K:
- Tamaño: ~3.5GB
- RAM necesaria: ~5GB
- Calidad: ~85%
- Velocidad: +100%
```

## Recursos de Aprendizaje

### Documentación Oficial

- [Meta Llama](https://ai.meta.com/llama/)
- [Ollama Docs](https://github.com/ollama/ollama)
- [LangChain Docs](https://python.langchain.com/)
- [Hugging Face](https://huggingface.co/docs)

### Cursos Recomendados

**Gratuitos:**
- [DeepLearning.AI - Generative AI](https://www.deeplearning.ai/short-courses/)
- [Fast.ai - Practical Deep Learning](https://course.fast.ai/)
- [Google - Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

**De Pago:**
- [Coursera - Natural Language Processing Specialization](https://www.coursera.org/specializations/natural-language-processing)
- [Udacity - AI Product Manager](https://www.udacity.com/course/ai-product-manager-nanodegree--nd088)

### Libros

**Técnicos:**
- "Attention Is All You Need" - Paper original de Transformers
- "Deep Learning" - Ian Goodfellow
- "Natural Language Processing with Transformers" - Lewis Tunstall

**Aplicados:**
- "Building LLM Apps" - Valentina Alto
- "Generative AI with LangChain" - Ben Auffarth
- "AI Engineering" - Chip Huyen

### Blogs y Newsletters

- [The Batch](https://www.deeplearning.ai/the-batch/) - DeepLearning.AI
- [Import AI](https://jack-clark.net/) - Jack Clark
- [The Gradient](https://thegradient.pub/)
- [Hugging Face Blog](https://huggingface.co/blog)

## Comunidades y Foros

### Internacionales

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) - Reddit
- [Ollama Discord](https://discord.gg/ollama)
- [Hugging Face Forums](https://discuss.huggingface.co/)
- [LangChain Discord](https://discord.gg/langchain)

### En Español

- [r/es_inteligencia_artificial](https://reddit.com/r/es_inteligencia_artificial)
- [IA en Español - Telegram](https://t.me/IAenEspanol)
- [Python México](https://www.facebook.com/groups/pythonmexico/)

### Eventos

- **Meta AI Developer Events**
- **PyData Conferences**
- **ICLR, NeurIPS, ICML** - Conferencias académicas
- **Meetups locales de IA/ML**

## Datasets Públicos

### Para Fine-Tuning en Español

```python
# Datasets de Hugging Face
datasets = [
    "bertin-project/alpaca-spanish",
    "somosnlp/somos-clean-alpaca-es",
    "mrm8488/alpaca-es",
    "clibrain/Spanish-WikiQA",
]

# Cargar con datasets library
from datasets import load_dataset

dataset = load_dataset("bertin-project/alpaca-spanish")
```

### Datos Generales

| Dataset | Tamaño | Idioma | Uso |
|---------|--------|--------|-----|
| Common Crawl | Petabytes | Multi | Preentrenamiento |
| Wikipedia | ~20GB | Multi | Conocimiento general |
| OpenWebText | ~40GB | EN | Preentrenamiento |
| C4 | ~750GB | Multi | Preentrenamiento |
| The Pile | ~800GB | EN | Investigación |

### Datasets Especializados

**Código:**
- The Stack
- CodeSearchNet
- GitHub Code

**Conversación:**
- ShareGPT
- OpenAssistant
- Anthropic HH-RLHF

**Español:**
- BETO datasets
- SQuAD-es
- XNLI-es

## Troubleshooting Avanzado

### Error: "Out of Memory"

```bash
# Solución 1: Usar modelo más pequeño
ollama pull llama3.2:1b

# Solución 2: Aumentar swap (Linux)
sudo dd if=/dev/zero of=/swapfile bs=1G count=8
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Solución 3: Usar cuantización más agresiva
ollama pull llama3.1:8b-q4_0
```

### Error: "Model not found"

```bash
# Verificar modelos instalados
ollama list

# Re-descargar modelo
ollama pull llama3.1:8b

# Verificar permisos (Linux/Mac)
ls -la ~/.ollama/models/

# Limpiar caché corrupto
rm -rf ~/.ollama/models/manifests/*
```

### Problema: Respuestas Lentas

```python
# Optimización 1: Reducir contexto
ollama.generate(
    model='llama3.1:8b',
    prompt=prompt,
    options={'num_ctx': 2048}  # En lugar de 128k
)

# Optimización 2: Usar modelo cuantizado
# Q4 es ~2x más rápido que Q8

# Optimización 3: Batch processing
# Procesar múltiples prompts juntos

# Optimización 4: GPU acceleration
# Verificar que Ollama use GPU
nvidia-smi  # NVIDIA
rocm-smi    # AMD
```

### Error: "Connection Refused"

```bash
# Verificar que Ollama esté corriendo
ps aux | grep ollama

# Iniciar Ollama
ollama serve

# Verificar puerto
lsof -i :11434  # Mac/Linux
netstat -ano | findstr :11434  # Windows

# Cambiar puerto
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

### Problema: Calidad de Respuestas

```python
# Ajustar temperature
# Más bajo = más predecible
# Más alto = más creativo
options = {
    'temperature': 0.1,  # Para respuestas precisas
    'top_p': 0.9,
    'top_k': 40
}

# Mejorar prompt
prompt = """Contexto: [proporciona contexto relevante]

Tarea: [describe claramente lo que quieres]

Formato esperado: [especifica el formato]

Restricciones: [añade limitaciones si es necesario]
"""

# Usar sistema de prompts
messages = [
    {
        'role': 'system',
        'content': 'Eres un experto en [dominio]. Responde de manera [estilo].'
    },
    {
        'role': 'user',
        'content': 'Tu pregunta aquí'
    }
]
```

## 📊 Benchmarks de Rendimiento

### Tokens por Segundo (promedio)

```
Hardware: RTX 3080 (10GB)
Modelo: Llama 3.1 8B Q4

Batch Size 1:  ~45 tokens/s
Batch Size 4:  ~120 tokens/s
Batch Size 8:  ~180 tokens/s

Hardware: M1 Pro (16GB)
Modelo: Llama 3.1 8B Q4

Batch Size 1:  ~28 tokens/s
Batch Size 4:  ~75 tokens/s

Hardware: CPU (i7-12700K, 32GB RAM)
Modelo: Llama 3.1 8B Q4

Batch Size 1:  ~12 tokens/s
Batch Size 4:  ~30 tokens/s
```

## 🔧 Scripts Útiles

### Verificación Completa del Sistema

```bash
#!/bin/bash
# check_system.sh

echo "=== Verificación del Sistema para Llama ==="
echo

echo "1. Ollama instalado:"
ollama --version

echo "2. Modelos disponibles:"
ollama list

echo "3. Python instalado:"
python3 --version

echo "4. Paquetes Python:"
pip list | grep -E "ollama|langchain|chromadb"

echo "5. Memoria disponible:"
free -h  # Linux
# vm_stat  # macOS

echo "6. Espacio en disco:"
df -h ~/.ollama

echo "7. GPU disponible:"
nvidia-smi 2>/dev/null || echo "No NVIDIA GPU"

echo
echo "=== Verificación completa ==="
```

### Benchmark de Modelos

```python
# benchmark.py
import time
import ollama
import statistics

def benchmark_model(model, prompts, num_runs=3):
    """Benchmark de un modelo"""
    times = []
    
    for _ in range(num_runs):
        for prompt in prompts:
            start = time.time()
            ollama.generate(model=model, prompt=prompt)
            elapsed = time.time() - start
            times.append(elapsed)
    
    return {
        'model': model,
        'avg_time': statistics.mean(times),
        'min_time': min(times),
        'max_time': max(times),
        'std_dev': statistics.stdev(times) if len(times) > 1 else 0
    }

# Uso
prompts = [
    "¿Qué es Python?",
    "Explica la teoría de la relatividad",
    "Dame una receta de tacos"
]

models = ['llama3.2:1b', 'llama3.2:3b', 'llama3.1:8b']

for model in models:
    try:
        result = benchmark_model(model, prompts)
        print(f"\nModelo: {result['model']}")
        print(f"Tiempo promedio: {result['avg_time']:.2f}s")
        print(f"Desv. estándar: {result['std_dev']:.2f}s")
    except Exception as e:
        print(f"Error con {model}: {e}")
```

---

## 📚 Referencias

- [Ollama GitHub](https://github.com/ollama/ollama)
- [Meta Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/)
- [LangChain Documentation](https://python.langchain.com/)
- [Hugging Face Hub](https://huggingface.co/)

## ➡️ Siguiente

Consulta el [Glosario](./glosario.md) para términos técnicos.
