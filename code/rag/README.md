# Ejemplos RAG (Retrieval-Augmented Generation)

Sistema de generación aumentada por recuperación usando Llama y ChromaDB.

## 📖 ¿Qué es RAG?

RAG combina:
- **Recuperación**: Buscar información relevante en documentos
- **Generación**: Usar Llama para generar respuestas basadas en esa información

Esto permite que el LLM responda preguntas sobre documentos específicos con mayor precisión.

## 📁 Contenido

- `simple_rag.py` - Sistema RAG básico
- `document_loader.py` - Cargador de documentos
- `advanced_rag.py` - RAG avanzado con LangChain
- `pdf_rag.py` - RAG para documentos PDF

## 🚀 Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Descargar modelo de Ollama
ollama pull llama3.2:3b
```

## 💡 Uso Básico

### Ejemplo Simple

```python
from simple_rag import SimpleRAG

# Crear sistema RAG
rag = SimpleRAG()

# Agregar documentos
documents = [
    "Llama es un modelo de IA de Meta.",
    "Ollama permite ejecutar LLMs localmente.",
]

rag.add_documents(documents)

# Hacer pregunta
response = rag.query("¿Qué es Ollama?")
print(response)
```

### Desde Línea de Comandos

```bash
# RAG simple
python simple_rag.py

# RAG con documentos PDF
python pdf_rag.py --file documento.pdf

# RAG avanzado
python advanced_rag.py --docs ./mis_documentos/
```

## 🔧 Configuración

### Ajustar Número de Resultados

```python
rag = SimpleRAG(n_results=5)  # Devuelve 5 documentos relevantes
```

### Cambiar Modelo

```python
rag = SimpleRAG(model="llama3.1:8b")
```

## 📚 Casos de Uso

1. **Q&A sobre Documentación**
   - Cargar manuales, documentación técnica
   - Responder preguntas específicas

2. **Análisis de Contratos**
   - Procesar documentos legales
   - Extraer información específica

3. **Knowledge Base Empresarial**
   - Centralizar conocimiento de la empresa
   - Chatbot interno

4. **Investigación Académica**
   - Procesar papers y artículos
   - Resumir y extraer información

## 🎯 Mejores Prácticas

1. **Chunking**: Divide documentos grandes en chunks de ~1000 caracteres
2. **Overlap**: Usa overlap de 200 caracteres entre chunks
3. **Metadata**: Agrega metadata (fuente, fecha, autor) a documentos
4. **Embeddings**: Usa modelo de embeddings apropiado
5. **Testing**: Prueba con preguntas conocidas primero

## 📊 Benchmarks

```
Documentos: 100
Chunks promedio: 500
Tiempo de indexación: ~2s
Tiempo de query: ~1s (con llama3.2:3b)
Precisión: ~85% en documentos técnicos
```

## 🔍 Troubleshooting

**Problema**: Respuestas poco relevantes
- Solución: Aumenta `n_results` o mejora chunking

**Problema**: Respuestas lentas
- Solución: Usa modelo más pequeño o aumenta chunks

**Problema**: Memoria insuficiente
- Solución: Procesa documentos en lotes

## 📚 Recursos

- [ChromaDB Docs](https://docs.trychroma.com/)
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering/)
- [Ollama Embeddings](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings)
