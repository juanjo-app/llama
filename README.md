# Build Your Own AI Stack con Llama 🦙

[![CI Status](https://github.com/majorjuanjo/llama/workflows/CI%20-%20Lint%20and%20Link%20Checker/badge.svg)](https://github.com/majorjuanjo/llama/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-CODE.md)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.md)
[![Spanish](https://img.shields.io/badge/Idioma-Español-green.svg)](README.md)

> Repositorio oficial del workshop "Build Your Own AI Stack con Llama" - Una iniciativa de **incMTY** + **Meta AI** + **Secretaría de Economía**

[🌐 Documentación](./docs/README.md) | [💻 Código](./code/) | [🎯 Casos de Uso](./cases/) | [🤝 Comunidad](./community/)

---

## 📚 Acerca de Este Proyecto

Este repositorio es un espejo público y alternativa al GitBook del workshop, diseñado para ser una guía completa y práctica sobre cómo construir tu propio stack de inteligencia artificial usando **Llama**, el modelo de lenguaje grande (LLM) de código abierto de Meta.

### 🎯 Objetivos

- Democratizar el acceso a la IA mediante herramientas de código abierto
- Proporcionar una guía completa en español para desarrolladores
- Crear una comunidad activa de practicantes de IA en LATAM
- Facilitar la implementación de soluciones de IA en producción

## 🗂️ Estructura del Repositorio

```
llama/
├── 📖 docs/              # Documentación completa del workshop
│   ├── README.md         # Índice de la documentación
│   ├── 00-portada.md     # Portada y bienvenida
│   ├── 01-capitulo-0.md  # Introducción al ecosistema
│   ├── 02-capitulo-1.md  # Fundamentos de Llama
│   ├── 03-capitulo-2.md  # Configuración del entorno
│   ├── 04-capitulo-3.md  # Construcción de aplicaciones
│   ├── 05-capitulo-4.md  # Casos de uso avanzados
│   ├── anexos.md         # Recursos adicionales
│   └── glosario.md       # Glosario de términos
│
├── 💻 code/              # Ejemplos de código
│   ├── ollama/           # Ejemplos con Ollama
│   │   ├── simple_chat.py
│   │   ├── streaming_response.py
│   │   └── model_info.py
│   └── rag/              # Sistemas RAG
│       └── simple_rag.py
│
├── 📋 templates/         # Plantillas de negocio
│   ├── canvas/           # Business Model Canvas
│   ├── 30-60-90/         # Planes de implementación
│   └── prompts/          # Biblioteca de prompts
│
├── 🎯 cases/             # Casos de uso reales
├── 🤝 community/         # Recursos de la comunidad
├── 🖼️ assets/            # Imágenes y recursos
└── ⚙️ .github/           # Configuración de GitHub
    ├── ISSUE_TEMPLATE/   # Templates de issues
    └── workflows/        # CI/CD pipelines
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8+
- Ollama instalado
- 8GB RAM mínimo (16GB recomendado)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/majorjuanjo/llama.git
cd llama

# Instalar Ollama (si no lo tienes)
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar un modelo de Llama
ollama pull llama3.2:3b

# Instalar dependencias Python (en carpeta code/)
cd code/ollama
pip install -r requirements.txt

# Ejecutar tu primer chatbot
python simple_chat.py
```

### Tu Primera Interacción

```python
import ollama

response = ollama.chat(
    model='llama3.2:3b',
    messages=[{
        'role': 'user',
        'content': '¿Qué es Llama?'
    }]
)

print(response['message']['content'])
```

## 📖 Contenido del Workshop

### Capítulos Principales

1. **[Introducción](./docs/01-capitulo-0.md)** - Ecosistema de IA y Llama
2. **[Fundamentos](./docs/02-capitulo-1.md)** - Arquitectura técnica y conceptos
3. **[Configuración](./docs/03-capitulo-2.md)** - Setup del entorno de desarrollo
4. **[Aplicaciones](./docs/04-capitulo-3.md)** - Construcción de apps con Llama
5. **[Avanzado](./docs/05-capitulo-4.md)** - Fine-tuning, RAG y producción

### Recursos Adicionales

- **[Anexos](./docs/anexos.md)** - Comandos, comparativas, troubleshooting
- **[Glosario](./docs/glosario.md)** - Terminología técnica de IA/LLMs
- **[Templates](./templates/)** - Plantillas de negocio y prompts
- **[Casos de Uso](./cases/)** - Implementaciones reales

## 💡 Ejemplos de Código

### Chatbot Simple

```python
# Ver: code/ollama/simple_chat.py
python code/ollama/simple_chat.py
```

### Sistema RAG

```python
# Ver: code/rag/simple_rag.py
from simple_rag import SimpleRAG

rag = SimpleRAG()
rag.add_documents(["Tu documento aquí"])
response = rag.query("¿Qué dice el documento?")
```

### API con FastAPI

```python
# Ver ejemplos completos en docs/04-capitulo-3.md
uvicorn api:app --reload
```

## 🎓 Para Quién Es Este Workshop

- 👨‍💻 **Desarrolladores** que quieren integrar IA en sus aplicaciones
- 🚀 **Emprendedores** construyendo startups de IA
- 🎓 **Estudiantes** aprendiendo sobre LLMs y IA
- 🏢 **Profesionales** implementando soluciones empresariales
- 🔬 **Investigadores** explorando aplicaciones de Llama

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Este es un proyecto impulsado por la comunidad.

1. Lee la [Guía de Contribución](CONTRIBUTING.md)
2. Revisa el [Código de Conducta](CODE_OF_CONDUCT.md)
3. Busca [issues abiertos](https://github.com/majorjuanjo/llama/issues) o crea uno nuevo
4. Haz un fork y envía un Pull Request

### Áreas donde Necesitamos Ayuda

- 📝 Mejorar documentación
- 💻 Agregar ejemplos de código
- 🐛 Reportar y corregir bugs
- 🌐 Traducciones
- 📊 Casos de uso reales
- 🎨 Diseño y UX

## 📄 Licencias

Este proyecto utiliza un sistema de licencias dual:

- **Código**: [MIT License](LICENSE-CODE.md) - Libre para uso comercial y personal
- **Documentación**: [CC BY 4.0](LICENSE-DOCS.md) - Libre para compartir y adaptar con atribución

### ¿Qué significa esto?

✅ Puedes usar el código en proyectos comerciales  
✅ Puedes modificar y redistribuir  
✅ Puedes usar la documentación en tus cursos/workshops  
⚠️ Debes dar atribución apropiada  

## 🌟 Créditos y Reconocimientos

### Organizadores

- **[incMTY](https://tec.mx/es/incmty)** - Tecnológico de Monterrey
- **[Meta AI](https://ai.meta.com/)** - Creadores de Llama
- **[Secretaría de Economía](https://www.gob.mx/se)** - Gobierno de México

### Contribuidores

Gracias a todos los que han contribuido a este proyecto:

<!-- Contributors list will be auto-generated -->

[Ver todos los contribuidores →](https://github.com/majorjuanjo/llama/graphs/contributors)

## 📞 Comunidad y Soporte

### Canales Oficiales

- 💬 **[GitHub Discussions](https://github.com/majorjuanjo/llama/discussions)** - Conversaciones y preguntas
- 🐛 **[GitHub Issues](https://github.com/majorjuanjo/llama/issues)** - Reportar bugs y solicitar features
- 📚 **[Documentación](./docs/README.md)** - Guías y tutoriales completos
- 👥 **[Comunidad](./community/README.md)** - Eventos, proyectos y recursos

### Redes Sociales

- LinkedIn: Próximamente
- Discord: Próximamente
- Twitter/X: Próximamente

## 📊 Estado del Proyecto

- ✅ Documentación completa
- ✅ Ejemplos de código
- ✅ Templates de negocio
- ✅ CI/CD configurado
- 🚧 GitHub Pages (en progreso)
- 🚧 Casos de uso detallados
- 📅 Tutoriales en video (planeado)

## 🗺️ Roadmap

### Q4 2025

- [x] Lanzamiento inicial del repositorio
- [x] Documentación base en español
- [x] Ejemplos de código básicos
- [ ] GitHub Pages configurado
- [ ] Primer workshop presencial

### Q1 2026

- [ ] Casos de uso avanzados
- [ ] Tutoriales en video
- [ ] Comunidad Discord
- [ ] Programa de embajadores

### Q2 2026 y más allá

- [ ] Certificaciones
- [ ] Hackathons
- [ ] Colaboraciones con universidades
- [ ] Expansión a otros países LATAM

## ❓ Preguntas Frecuentes

**P: ¿Necesito experiencia previa en IA?**  
R: No, el workshop está diseñado para todos los niveles. Comenzamos desde lo básico.

**P: ¿Es gratis?**  
R: Sí, todo el contenido es completamente gratuito y de código abierto.

**P: ¿Funciona en mi computadora?**  
R: Si tienes 8GB+ de RAM y una CPU moderna, sí. GPU es opcional.

**P: ¿Puedo usar esto comercialmente?**  
R: Sí, la licencia MIT permite uso comercial del código.

[Ver más FAQs →](./community/FAQ.md)

## 📚 Recursos Externos

### Documentación Oficial

- [Meta Llama](https://ai.meta.com/llama/)
- [Ollama](https://ollama.ai/)
- [LangChain](https://python.langchain.com/)

### Cursos Complementarios

- [DeepLearning.AI](https://www.deeplearning.ai/)
- [Fast.ai](https://www.fast.ai/)
- [Hugging Face Course](https://huggingface.co/learn)

## 🙏 Agradecimientos Especiales

A todos los que han contribuido con su tiempo, conocimiento y entusiasmo para hacer de este proyecto una realidad.

---

<div align="center">

**¿Listo para construir tu propio AI Stack?**

[📖 Comenzar con la Documentación](./docs/README.md) | [💻 Ver Ejemplos de Código](./code/) | [🤝 Unirse a la Comunidad](./community/)

---

Hecho con ❤️ por la comunidad | [Contribuir](CONTRIBUTING.md) | [Código de Conducta](CODE_OF_CONDUCT.md)

**Última actualización**: Octubre 2025 | **Versión**: 1.0.0

</div>