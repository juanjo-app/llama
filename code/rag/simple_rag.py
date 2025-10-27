#!/usr/bin/env python3
"""
Sistema RAG simple usando ChromaDB y Ollama
"""

import chromadb
from chromadb.utils import embedding_functions
import ollama


class SimpleRAG:
    """
    Sistema de Retrieval-Augmented Generation básico
    """
    
    def __init__(
        self,
        collection_name="knowledge_base",
        model="llama3.2:3b",
        n_results=3
    ):
        """
        Inicializar sistema RAG
        
        Args:
            collection_name: Nombre de la colección en ChromaDB
            model: Modelo de Llama a usar
            n_results: Número de documentos a recuperar
        """
        self.model = model
        self.n_results = n_results
        
        # Inicializar ChromaDB
        self.client = chromadb.Client()
        
        # Función de embedding por defecto
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
        
        # Crear o obtener colección
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )
    
    def add_documents(self, documents, metadatas=None, ids=None):
        """
        Agregar documentos a la base de conocimiento
        
        Args:
            documents: Lista de textos
            metadatas: Lista de metadata (opcional)
            ids: Lista de IDs (opcional, se generan automáticamente)
        """
        if ids is None:
            # Generar IDs únicos
            existing_count = self.collection.count()
            ids = [f"doc_{i}" for i in range(existing_count, existing_count + len(documents))]
        
        # Agregar a la colección
        self.collection.add(
            documents=documents,
            metadatas=metadatas if metadatas else [{"source": "unknown"}] * len(documents),
            ids=ids
        )
        
        print(f"✓ Agregados {len(documents)} documentos")
    
    def search(self, query, n_results=None):
        """
        Buscar documentos relevantes
        
        Args:
            query: Texto de búsqueda
            n_results: Número de resultados (opcional)
        
        Returns:
            Documentos relevantes
        """
        if n_results is None:
            n_results = self.n_results
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        return results
    
    def query(self, question, use_context=True, temperature=0.7):
        """
        Hacer pregunta con o sin contexto
        
        Args:
            question: Pregunta a responder
            use_context: Si usar contexto de documentos
            temperature: Creatividad de la respuesta
        
        Returns:
            Respuesta generada
        """
        if use_context:
            # Buscar documentos relevantes
            results = self.search(question)
            documents = results['documents'][0] if results['documents'] else []
            
            if not documents:
                return "No encontré información relevante para responder tu pregunta."
            
            # Construir contexto
            context = "\n\n".join(documents)
            
            # Construir prompt con contexto
            prompt = f"""Basándote en el siguiente contexto, responde la pregunta de manera precisa y concisa.
Si la información no está en el contexto, indica que no tienes suficiente información.

Contexto:
{context}

Pregunta: {question}

Respuesta:"""
        else:
            prompt = question
        
        # Generar respuesta con Llama
        try:
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={
                    'temperature': temperature
                }
            )
            
            return response['response']
        
        except Exception as e:
            return f"Error al generar respuesta: {e}"
    
    def chat_with_context(self):
        """
        Modo chat interactivo con contexto
        """
        print(f"🤖 RAG Chat con {self.model}")
        print(f"📚 Documentos en base: {self.collection.count()}")
        print("Escribe 'salir' para terminar\n")
        
        while True:
            try:
                question = input("Pregunta: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n¡Hasta luego!")
                break
            
            if question.lower() in ['salir', 'exit', 'quit', 'q']:
                print("¡Hasta luego!")
                break
            
            if not question:
                continue
            
            # Buscar y mostrar documentos relevantes
            print("\n🔍 Buscando información relevante...")
            results = self.search(question)
            
            if results['documents'][0]:
                print(f"✓ Encontrados {len(results['documents'][0])} documentos relevantes\n")
            
            # Generar respuesta
            print("🤖 Respuesta:")
            response = self.query(question)
            print(response)
            print()


def main():
    """Ejemplo de uso"""
    
    # Crear sistema RAG
    rag = SimpleRAG()
    
    # Documentos de ejemplo sobre Llama y IA
    documents = [
        "Llama es una familia de modelos de lenguaje grandes desarrollada por Meta AI. Los modelos están disponibles en varios tamaños, desde 1B hasta 405B parámetros.",
        "Ollama es una herramienta que permite ejecutar modelos de lenguaje grandes localmente en tu computadora. Soporta modelos como Llama, Mistral y otros.",
        "RAG (Retrieval-Augmented Generation) es una técnica que combina búsqueda de información con generación de texto para producir respuestas más precisas y fundamentadas.",
        "ChromaDB es una base de datos vectorial diseñada para almacenar y buscar embeddings de manera eficiente. Es ideal para aplicaciones de IA como RAG.",
        "El fine-tuning es el proceso de adaptar un modelo preentrenado a un caso de uso específico mediante entrenamiento adicional con datos especializados.",
        "La temperatura es un parámetro que controla la aleatoriedad en la generación de texto. Valores bajos (0.1-0.3) producen respuestas más deterministas.",
        "Los embeddings son representaciones vectoriales de texto que capturan significado semántico. Textos similares tienen embeddings cercanos en el espacio vectorial.",
        "Python es el lenguaje más popular para desarrollo de IA y machine learning, con bibliotecas como LangChain, ChromaDB y Ollama.",
    ]
    
    # Metadata para cada documento
    metadatas = [
        {"topic": "llama", "category": "models"},
        {"topic": "ollama", "category": "tools"},
        {"topic": "rag", "category": "techniques"},
        {"topic": "chromadb", "category": "tools"},
        {"topic": "fine-tuning", "category": "techniques"},
        {"topic": "parameters", "category": "techniques"},
        {"topic": "embeddings", "category": "concepts"},
        {"topic": "python", "category": "programming"},
    ]
    
    # Agregar documentos
    print("📚 Cargando documentos...\n")
    rag.add_documents(documents, metadatas=metadatas)
    
    # Ejemplos de consultas
    print("\n" + "="*50)
    print("Ejemplos de Consultas")
    print("="*50 + "\n")
    
    questions = [
        "¿Qué es Ollama?",
        "¿Cómo funciona RAG?",
        "¿Qué tamaños tiene Llama?",
    ]
    
    for question in questions:
        print(f"❓ {question}")
        response = rag.query(question)
        print(f"💡 {response}\n")
    
    # Modo interactivo
    print("\n" + "="*50)
    print("Modo Interactivo")
    print("="*50 + "\n")
    
    rag.chat_with_context()


if __name__ == "__main__":
    main()
