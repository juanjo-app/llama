# Referencia Rápida - Llama Workshop

> Guía de referencia rápida para comandos y conceptos comunes

## 🚀 Comandos Esenciales

### Ollama

```bash
# Gestión de modelos
ollama list                    # Listar modelos instalados
ollama pull llama3.2:3b       # Descargar modelo
ollama rm llama3.2:3b         # Eliminar modelo
ollama show llama3.2:3b       # Info del modelo

# Ejecutar modelos
ollama run llama3.2:3b        # Modo interactivo
ollama run llama3.2:3b "prompt"  # Prompt directo

# Servidor
ollama serve                  # Iniciar servidor
```

### Python - Ollama

```python
import ollama

# Chat básico
response = ollama.chat(
    model='llama3.2:3b',
    messages=[{'role': 'user', 'content': 'Hola'}]
)

# Generación simple
response = ollama.generate(
    model='llama3.2:3b',
    prompt='Escribe un haiku'
)

# Streaming
for chunk in ollama.chat(model='llama3.2:3b', messages=msgs, stream=True):
    print(chunk['message']['content'], end='')
```

### Git

```bash
# Actualizar repositorio
git pull origin main

# Ver estado
git status

# Crear rama
git checkout -b mi-feature

# Commit y push
git add .
git commit -m "Descripción"
git push origin mi-feature
```

## 📊 Parámetros Comunes

### Temperature
```
0.1-0.3  → Respuestas precisas, deterministas
0.4-0.7  → Balanceado (default)
0.8-1.2  → Creativo, variado
1.3-2.0  → Muy creativo, impredecible
```

### Top-P (Nucleus Sampling)
```
0.9-0.95 → Recomendado (default)
0.8      → Más conservador
0.99     → Más diverso
```

### Top-K
```
40-50    → Recomendado
20-30    → Más conservador
60-80    → Más diverso
```

## 🗂️ Estructura de Prompts

### Formato Básico
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

[Tu sistema prompt aquí]<|eot_id|><|start_header_id|>user<|end_header_id|>

[Tu pregunta aquí]<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

### Template Efectivo
```
Rol: Eres un [rol específico]
Contexto: [información relevante]
Tarea: [qué debe hacer]
Formato: [cómo debe responder]
Restricciones: [limitaciones]

[Input del usuario]
```

## 📚 Navegación Rápida

### Documentación
- [Inicio](README.md)
- [Getting Started](GETTING_STARTED.md)
- [Docs principales](docs/README.md)
- [Glosario](docs/glosario.md)
- [Anexos](docs/anexos.md)

### Código
- [Ollama ejemplos](code/ollama/)
- [RAG ejemplos](code/rag/)

### Templates
- [Business Canvas](templates/canvas/)
- [Plan 30-60-90](templates/30-60-90/)
- [Prompts](templates/prompts/)

### Comunidad
- [Contribuir](CONTRIBUTING.md)
- [Código de Conducta](CODE_OF_CONDUCT.md)
- [Issues](https://github.com/majorjuanjo/llama/issues)
- [Discussions](https://github.com/majorjuanjo/llama/discussions)

## 🔧 Troubleshooting Rápido

| Error | Solución Rápida |
|-------|----------------|
| "ollama not found" | Reinicia terminal o agrega a PATH |
| "model not found" | `ollama pull nombre-modelo` |
| "out of memory" | Usa modelo más pequeño (1b o 3b) |
| "connection refused" | `ollama serve` en otra terminal |
| "module not found" | `pip install -r requirements.txt` |

## 💡 Tips Rápidos

### Mejorar Respuestas
1. Sé específico en tus prompts
2. Proporciona ejemplos (few-shot)
3. Ajusta temperature según necesidad
4. Usa sistema de prompts para contexto

### Optimizar Performance
1. Usa cuantización apropiada (Q4, Q5, Q8)
2. Limita context window si no necesitas 128k
3. Batch requests cuando sea posible
4. Cachea respuestas comunes

### Mejores Prácticas
1. Siempre maneja errores
2. Valida inputs del usuario
3. Limita longitud de respuestas
4. Monitorea uso de recursos
5. Documenta tus prompts

## 📊 Tamaños de Modelo

| Modelo | Parámetros | RAM | Uso |
|--------|-----------|-----|-----|
| llama3.2:1b | 1B | 2GB | Móvil, Edge |
| llama3.2:3b | 3B | 4GB | Chat general |
| llama3.1:8b | 8B | 8GB | Propósito general |
| llama3.1:70b | 70B | 48GB | Tareas complejas |

## 🎯 Casos de Uso Comunes

### Chatbot
```python
from code.ollama import simple_chat
# Ver: code/ollama/simple_chat.py
```

### RAG
```python
from code.rag import simple_rag
# Ver: code/rag/simple_rag.py
```

### API
```python
from fastapi import FastAPI
# Ver: docs/04-capitulo-3.md
```

## 📞 Soporte

- 📖 [Documentación completa](docs/)
- 🐛 [Reportar bug](https://github.com/majorjuanjo/llama/issues/new?template=bug_report.md)
- 💡 [Solicitar feature](https://github.com/majorjuanjo/llama/issues/new?template=feature_request.md)
- ❓ [Hacer pregunta](https://github.com/majorjuanjo/llama/issues/new?template=question.md)

## 🔗 Enlaces Útiles

- [Ollama Docs](https://github.com/ollama/ollama)
- [Meta Llama](https://ai.meta.com/llama/)
- [LangChain](https://python.langchain.com/)
- [ChromaDB](https://docs.trychroma.com/)

---

**💾 Guarda esta página como favorito para referencia rápida**

[🏠 Volver al README](README.md)
