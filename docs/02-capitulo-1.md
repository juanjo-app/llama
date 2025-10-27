# Capítulo 1: Fundamentos de Llama

## 📖 Contenido

1. [Arquitectura Técnica](#arquitectura-técnica)
2. [Formato de Prompts](#formato-de-prompts)
3. [Parámetros de Generación](#parámetros-de-generación)
4. [Cuantización](#cuantización)
5. [Optimización de Rendimiento](#optimización-de-rendimiento)

---

## Arquitectura Técnica

### Transformer Architecture

Llama se basa en la arquitectura Transformer con las siguientes optimizaciones:

- **RMSNorm**: Normalización mejorada para entrenamiento estable
- **SwiGLU**: Función de activación optimizada
- **RoPE**: Positional embeddings rotacionales
- **Grouped Query Attention**: Reducción de memoria en inferencia

### Especificaciones Técnicas

```
Llama 3.1 8B:
- Parámetros: 8 mil millones
- Capas: 32
- Dimensión oculta: 4096
- Cabezas de atención: 32
- Vocabulario: 128,256 tokens
- Longitud de contexto: 128k tokens
```

## Formato de Prompts

### Plantilla de Sistema

Llama utiliza tokens especiales para estructurar conversaciones:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Eres un asistente útil.<|eot_id|><|start_header_id|>user<|end_header_id|>

¿Cuál es la capital de México?<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

### Mejores Prácticas para Prompts

1. **Sé Específico**
   ```
   ❌ Malo: "Escribe sobre México"
   ✅ Bueno: "Escribe un párrafo de 100 palabras sobre la historia prehispánica de México"
   ```

2. **Proporciona Contexto**
   ```
   ✅ "Como experto en finanzas mexicanas, explica qué es el ISR..."
   ```

3. **Usa Ejemplos (Few-Shot)**
   ```
   Clasifica el sentimiento:
   
   Texto: "Me encantó el producto"
   Sentimiento: Positivo
   
   Texto: "No funcionó como esperaba"
   Sentimiento: Negativo
   
   Texto: "El servicio es excelente"
   Sentimiento: [Tu respuesta aquí]
   ```

## Parámetros de Generación

### Parámetros Principales

| Parámetro | Rango | Descripción | Uso Recomendado |
|-----------|-------|-------------|-----------------|
| `temperature` | 0.0-2.0 | Creatividad vs Precisión | 0.1-0.3 (preciso), 0.7-1.0 (creativo) |
| `top_p` | 0.0-1.0 | Nucleus sampling | 0.9-0.95 |
| `top_k` | 1-100 | Limitación de vocabulario | 40-50 |
| `max_tokens` | 1-128000 | Longitud máxima | Según necesidad |
| `repeat_penalty` | 1.0-2.0 | Evita repeticiones | 1.1-1.2 |

### Ejemplos de Configuración

```python
# Para respuestas precisas (documentación, código)
{
    "temperature": 0.1,
    "top_p": 0.95,
    "top_k": 40,
    "max_tokens": 2000
}

# Para contenido creativo (historias, marketing)
{
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 50,
    "max_tokens": 1000
}

# Para conversación balanceada
{
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_tokens": 500
}
```

## Cuantización

La cuantización reduce el tamaño del modelo manteniendo calidad aceptable.

### Tipos de Cuantización

| Formato | Precisión | Tamaño vs FP16 | Calidad | Velocidad |
|---------|-----------|----------------|---------|-----------|
| FP16 | 16-bit | 100% | Excelente | Lenta |
| Q8 | 8-bit | ~50% | Muy buena | Media |
| Q5 | 5-bit | ~31% | Buena | Rápida |
| Q4 | 4-bit | ~25% | Aceptable | Muy rápida |
| Q2 | 2-bit | ~12.5% | Limitada | Extremadamente rápida |

### Recomendaciones de Cuantización

```
Llama 3.1 8B:
- Producción: Q8 o Q5_K_M
- Desarrollo: Q4_K_M
- Edge/Móvil: Q4_0 o Q2_K

Llama 3.1 70B:
- Producción: Q5_K_M
- Desarrollo: Q4_K_M
```

## Optimización de Rendimiento

### 1. Hardware

**CPU**:
- AMD Ryzen 7/9 o Intel i7/i9
- Mínimo 8 núcleos recomendado

**GPU** (opcional pero recomendado):
- NVIDIA: RTX 3060+ (12GB VRAM mínimo)
- AMD: RX 6800+ 
- Apple: M1 Pro+ (Metal acceleration)

**RAM**:
- 8B model: 16GB mínimo, 32GB recomendado
- 70B model: 64GB+ mínimo

### 2. Configuración de Sistema

```bash
# Linux: Aumentar límites de memoria
ulimit -l unlimited

# Optimizar swap
sudo sysctl vm.swappiness=10

# Para modelos grandes (70B+)
sudo sysctl vm.overcommit_memory=1
```

### 3. Batch Processing

```python
# Procesar múltiples prompts eficientemente
prompts = [
    "Pregunta 1...",
    "Pregunta 2...",
    "Pregunta 3..."
]

# Procesamiento en lotes reduce overhead
responses = model.generate(prompts, batch_size=3)
```

### 4. Context Management

```python
# Limita el contexto para mejor rendimiento
max_context = 4096  # En lugar de 128k para respuestas rápidas

# Usa sliding window para conversaciones largas
if len(conversation) > max_context:
    conversation = conversation[-max_context:]
```

## 🎯 Ejercicio Práctico

1. **Experimenta con Temperature**:
   - Genera 5 respuestas con temperature=0.1
   - Genera 5 respuestas con temperature=1.5
   - Compara la variabilidad

2. **Cuantización**:
   - Calcula cuánta RAM necesitas para Llama 8B en Q4 vs Q8
   - ¿Qué formato es adecuado para tu hardware?

3. **Diseño de Prompt**:
   - Diseña un prompt efectivo para tu caso de uso
   - Incluye contexto, ejemplos y formato esperado

---

## 📚 Recursos Técnicos

- [Llama Model Card](https://github.com/meta-llama/llama-models)
- [GGUF Format Documentation](https://github.com/ggerganov/ggml)
- [Optimization Techniques](https://huggingface.co/docs/transformers/llm_tutorial_optimization)

## ➡️ Siguiente Paso

Avanza al [Capítulo 2: Configuración del Entorno](./03-capitulo-2.md) para comenzar con la instalación práctica.
