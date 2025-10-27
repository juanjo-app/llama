# Contribuyendo a Llama Workshop

¡Gracias por tu interés en contribuir! 🎉

Este documento proporciona pautas para contribuir al repositorio del workshop "Build Your Own AI Stack con Llama".

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [Cómo Puedo Contribuir](#cómo-puedo-contribuir)
- [Guía de Estilo](#guía-de-estilo)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Estructura del Proyecto](#estructura-del-proyecto)

## Código de Conducta

Este proyecto y todos los participantes están regidos por nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que respetes este código.

## Cómo Puedo Contribuir

### 🐛 Reportar Bugs

Si encuentras un bug:

1. Verifica que no exista un issue similar
2. Usa la plantilla de bug report
3. Incluye:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Screenshots si aplica
   - Versiones (OS, Python, Ollama, etc.)

### 💡 Sugerir Mejoras

Para nuevas funcionalidades o mejoras:

1. Verifica que no exista un issue similar
2. Usa la plantilla de feature request
3. Describe claramente:
   - El problema que resuelve
   - La solución propuesta
   - Alternativas consideradas

### 📝 Mejorar Documentación

La documentación siempre puede mejorar:

- Corregir errores tipográficos o gramaticales
- Aclarar explicaciones confusas
- Agregar ejemplos adicionales
- Traducir contenido (si aplica)
- Mejorar la estructura

### 💻 Contribuir Código

#### Áreas de Contribución

- **Ejemplos de código**: Nuevos casos de uso o mejoras
- **Herramientas**: Scripts útiles para la comunidad
- **Tests**: Aumentar cobertura de pruebas
- **Optimizaciones**: Mejorar rendimiento
- **Casos de uso**: Documentar implementaciones reales

#### Antes de Empezar

1. **Fork** el repositorio
2. **Clone** tu fork localmente
3. **Crea una rama** desde `main`
4. **Configura** tu entorno de desarrollo

```bash
# Clone tu fork
git clone https://github.com/TU_USUARIO/llama.git
cd llama

# Agrega el repositorio original como upstream
git remote add upstream https://github.com/majorjuanjo/llama.git

# Crea una rama para tu contribución
git checkout -b feature/tu-funcionalidad
```

## Guía de Estilo

### Código Python

Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/):

```python
# Bueno
def process_documents(documents, max_tokens=1000):
    """
    Procesa lista de documentos.
    
    Args:
        documents: Lista de textos a procesar
        max_tokens: Longitud máxima por chunk
    
    Returns:
        Lista de chunks procesados
    """
    chunks = []
    for doc in documents:
        # Lógica de procesamiento
        pass
    return chunks

# Evitar
def processDocuments(docs,maxTokens=1000):
    chunks=[]
    for d in docs:
        pass
    return chunks
```

### Documentación

- **Idioma principal**: Español
- **Formato**: Markdown
- **Tono**: Claro, educativo, inclusivo
- **Ejemplos**: Siempre que sea posible

#### Estructura de Documentos

```markdown
# Título Principal

Breve introducción de qué trata el documento.

## 📖 Contenido

1. [Sección 1](#sección-1)
2. [Sección 2](#sección-2)

---

## Sección 1

Contenido...

### Subsección

Contenido...

## Sección 2

Contenido...

---

## 📚 Recursos

- [Enlace 1](url)
- [Enlace 2](url)
```

### Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Formato
<tipo>(<alcance>): <descripción>

# Ejemplos
feat(docs): agregar capítulo sobre fine-tuning
fix(rag): corregir búsqueda de documentos vacíos
docs(readme): actualizar instrucciones de instalación
chore(deps): actualizar dependencias
```

**Tipos**:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, punto y coma faltante, etc.
- `refactor`: Refactorización de código
- `test`: Agregar o modificar tests
- `chore`: Cambios en build, dependencias, etc.

## Proceso de Pull Request

### 1. Antes de Crear el PR

- [ ] Tu código sigue la guía de estilo
- [ ] Has agregado tests si aplica
- [ ] La documentación está actualizada
- [ ] Todos los tests pasan localmente
- [ ] Has probado tu cambio en tu entorno

### 2. Crear el Pull Request

1. **Push** tu rama a tu fork
2. Ve a GitHub y crea el **Pull Request**
3. Usa la plantilla de PR
4. Describe claramente:
   - Qué cambios incluye
   - Por qué son necesarios
   - Cómo probaste los cambios
   - Screenshots si aplica

### 3. Plantilla de PR

```markdown
## Descripción

Breve descripción de los cambios.

## Tipo de Cambio

- [ ] Bug fix
- [ ] Nueva funcionalidad
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha probado?

Describe las pruebas realizadas.

## Checklist

- [ ] Mi código sigue la guía de estilo
- [ ] He realizado self-review
- [ ] He comentado código complejo
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan nuevos warnings
- [ ] He agregado tests
- [ ] Tests nuevos y existentes pasan localmente
```

### 4. Revisión

- Mantén el PR enfocado (un cambio a la vez)
- Responde a comentarios constructivamente
- Haz los cambios solicitados
- Mantén conversación profesional

### 5. Después de la Aprobación

- El maintainer hará merge del PR
- Puedes borrar tu rama
- ¡Celebra! 🎉

## Estructura del Proyecto

```
llama/
├── docs/               # Documentación del workshop
│   ├── README.md
│   ├── 00-portada.md
│   ├── 01-capitulo-0.md
│   └── ...
├── code/              # Ejemplos de código
│   ├── ollama/        # Ejemplos con Ollama
│   └── rag/           # Ejemplos de RAG
├── templates/         # Plantillas de negocio
│   ├── canvas/
│   ├── 30-60-90/
│   └── prompts/
├── cases/             # Casos de uso
├── community/         # Recursos de comunidad
├── assets/            # Imágenes, recursos
└── .github/           # Templates de GitHub
```

## Áreas que Necesitan Ayuda

Revisa los [issues etiquetados](https://github.com/majorjuanjo/llama/labels/help%20wanted):

- `good first issue`: Ideal para nuevos contribuidores
- `help wanted`: Necesitamos ayuda
- `documentation`: Mejoras a docs
- `enhancement`: Nuevas funcionalidades

## Reconocimiento

Todos los contribuidores serán reconocidos en:

- README principal
- Sección de contribuidores
- Release notes (si aplica)

## Preguntas

¿Tienes dudas? 

- Abre un [Discussion](https://github.com/majorjuanjo/llama/discussions)
- Revisa [issues existentes](https://github.com/majorjuanjo/llama/issues)
- Contacta a los maintainers

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo:

- **Código**: MIT License
- **Documentación**: CC BY 4.0

---

**¡Gracias por contribuir! Tu ayuda hace que este proyecto sea mejor para todos.** 🙏
