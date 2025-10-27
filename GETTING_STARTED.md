# Guía de Inicio Rápido 🚀

Bienvenido al workshop "Build Your Own AI Stack con Llama". Esta guía te ayudará a empezar en minutos.

## ⏱️ Tiempo Estimado

- **Setup básico**: 10-15 minutos
- **Primer ejemplo**: 5 minutos
- **Exploración completa**: 1-2 horas

## 📋 Antes de Empezar

### Verificar Requisitos

```bash
# Python (debe ser 3.8+)
python3 --version

# Espacio en disco (necesitas al menos 10GB libres)
df -h

# Memoria RAM (recomendado 8GB+)
# Linux: free -h
# macOS: system_profiler SPHardwareDataType | grep Memory
# Windows: systeminfo | find "Total Physical Memory"
```

## 🛠️ Instalación Paso a Paso

### Paso 1: Clonar el Repositorio

```bash
# Opción A: HTTPS
git clone https://github.com/majorjuanjo/llama.git

# Opción B: SSH
git clone git@github.com:majorjuanjo/llama.git

# Entrar al directorio
cd llama
```

### Paso 2: Instalar Ollama

#### macOS

```bash
# Opción A: Descarga directa
# Ve a https://ollama.ai y descarga el instalador

# Opción B: Homebrew
brew install ollama
```

#### Linux

```bash
# Script oficial de instalación
curl -fsSL https://ollama.ai/install.sh | sh

# Verificar instalación
ollama --version
```

#### Windows

```bash
# Descarga el instalador desde https://ollama.ai
# Ejecuta el instalador y sigue las instrucciones

# Verifica en PowerShell o CMD
ollama --version
```

### Paso 3: Descargar un Modelo

```bash
# Modelo pequeño para comenzar (recomendado)
ollama pull llama3.2:3b

# Alternativas según tu hardware:
# 1GB RAM: ollama pull llama3.2:1b
# 8GB RAM: ollama pull llama3.1:8b
# 48GB RAM: ollama pull llama3.1:70b

# Verificar modelos descargados
ollama list
```

### Paso 4: Configurar Python

```bash
# Crear entorno virtual (recomendado)
python3 -m venv venv

# Activar entorno virtual
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Actualizar pip
pip install --upgrade pip
```

### Paso 5: Instalar Dependencias

```bash
# Para ejemplos de Ollama
cd code/ollama
pip install -r requirements.txt

# Para ejemplos de RAG
cd ../rag
pip install -r requirements.txt

# Volver al directorio raíz
cd ../..
```

## ✅ Verificar Instalación

### Test 1: Ollama CLI

```bash
# Prueba rápida en terminal
ollama run llama3.2:3b "Hola, ¿cómo estás?"

# Deberías ver una respuesta del modelo
# Presiona Ctrl+D o escribe /bye para salir
```

### Test 2: Script de Python

```bash
# Desde el directorio raíz del proyecto
python3 code/ollama/simple_chat.py

# Deberías ver:
# 🤖 Chatbot Simple con Llama
# ✓ Modelo cargado. ¡Comencemos!
```

### Test 3: Información del Sistema

```bash
python3 code/ollama/model_info.py --list

# Deberías ver la lista de modelos instalados
```

## 🎯 Tus Primeros Pasos

### 1. Chatbot Interactivo (5 min)

```bash
cd code/ollama
python simple_chat.py

# Prueba preguntas como:
# - ¿Qué es Python?
# - Explica qué es la IA
# - Escribe un haiku sobre programación
```

### 2. Streaming de Respuestas (5 min)

```bash
python streaming_response.py

# Observa cómo se genera el texto token por token
```

### 3. Sistema RAG Básico (10 min)

```bash
cd ../rag
python simple_rag.py

# El script:
# 1. Carga documentos de ejemplo
# 2. Crea índice de búsqueda
# 3. Permite hacer preguntas sobre los documentos
```

### 4. Explorar la Documentación (30 min)

```bash
# Abre en tu navegador o editor favorito
# Comienza con la portada
cat docs/00-portada.md

# O navega por GitHub:
# https://github.com/majorjuanjo/llama/tree/main/docs
```

## 📚 Rutas de Aprendizaje

### Para Principiantes

1. ✅ [Portada](docs/00-portada.md) - Conoce el workshop
2. ✅ [Capítulo 0](docs/01-capitulo-0.md) - Introducción a IA y Llama
3. ✅ [Capítulo 2](docs/03-capitulo-2.md) - Configuración (ya la hiciste!)
4. ✅ [Glosario](docs/glosario.md) - Términos clave
5. ✅ Experimenta con `code/ollama/simple_chat.py`

### Para Desarrolladores

1. ✅ [Capítulo 1](docs/02-capitulo-1.md) - Fundamentos técnicos
2. ✅ [Capítulo 3](docs/04-capitulo-3.md) - Construcción de apps
3. ✅ [Capítulo 4](docs/05-capitulo-4.md) - Casos avanzados
4. ✅ Explora ejemplos en `code/`
5. ✅ Lee [Anexos](docs/anexos.md) para troubleshooting

### Para Emprendedores

1. ✅ [Templates de Canvas](templates/canvas/)
2. ✅ [Plan 30-60-90](templates/30-60-90/)
3. ✅ [Casos de Uso](cases/)
4. ✅ [Biblioteca de Prompts](templates/prompts/)

## 🔧 Personalización

### Cambiar de Modelo

```bash
# En cualquier script Python, cambia:
model = "llama3.2:3b"

# Por:
model = "llama3.1:8b"    # Más potente
# o
model = "llama3.2:1b"    # Más rápido
```

### Ajustar Parámetros

```python
# En tus scripts, modifica:
response = ollama.chat(
    model='llama3.2:3b',
    messages=messages,
    options={
        'temperature': 0.7,  # Cambia entre 0.1 (preciso) y 1.5 (creativo)
        'top_p': 0.9,
        'top_k': 40
    }
)
```

## ❓ Problemas Comunes

### "ollama: command not found"

**Solución**: Reinicia tu terminal después de instalar Ollama

```bash
# O especifica la ruta completa
/usr/local/bin/ollama --version  # macOS/Linux
```

### "Model not found"

**Solución**: Descarga el modelo primero

```bash
ollama pull llama3.2:3b
ollama list  # Verifica que se descargó
```

### "Out of Memory"

**Solución**: Usa un modelo más pequeño

```bash
ollama pull llama3.2:1b  # Solo 1GB RAM necesaria
```

### "Module not found"

**Solución**: Instala las dependencias

```bash
pip install -r code/ollama/requirements.txt
```

### "Connection refused"

**Solución**: Inicia Ollama manualmente

```bash
# En una terminal separada
ollama serve

# En otra terminal, ejecuta tu script
python code/ollama/simple_chat.py
```

## 📞 Obtener Ayuda

Si tienes problemas:

1. 📖 Consulta [Troubleshooting en Anexos](docs/anexos.md#troubleshooting-avanzado)
2. 🔍 Busca en [Issues](https://github.com/majorjuanjo/llama/issues)
3. 💬 Pregunta en [Discussions](https://github.com/majorjuanjo/llama/discussions)
4. 📝 Crea un [Issue nuevo](https://github.com/majorjuanjo/llama/issues/new/choose)

## 🎓 Próximos Pasos

Una vez que hayas completado la configuración:

### Semana 1
- [ ] Completa Capítulos 0-2
- [ ] Ejecuta todos los ejemplos de `code/ollama/`
- [ ] Experimenta con diferentes prompts

### Semana 2
- [ ] Lee Capítulos 3-4
- [ ] Implementa tu primer sistema RAG
- [ ] Crea un chatbot personalizado

### Semana 3
- [ ] Explora casos de uso avanzados
- [ ] Integra Llama en un proyecto personal
- [ ] Comparte tu proyecto en la comunidad

### Mes 2
- [ ] Contribuye al repositorio
- [ ] Participa en discusiones
- [ ] Ayuda a otros usuarios

## 🌟 Consejos de Éxito

1. **Comienza simple**: No intentes todo a la vez
2. **Practica diario**: 30 minutos al día > 3 horas el fin de semana
3. **Experimenta**: Cambia parámetros y observa resultados
4. **Documenta**: Guarda tus hallazgos y experimentos
5. **Comparte**: Participa en la comunidad

## 🎯 Checklist de Inicio

- [ ] Repositorio clonado
- [ ] Ollama instalado y funcionando
- [ ] Modelo descargado (llama3.2:3b o similar)
- [ ] Entorno virtual de Python creado
- [ ] Dependencias instaladas
- [ ] Chatbot simple ejecutado exitosamente
- [ ] Documentación explorada
- [ ] Primeros ejemplos probados

## 🎉 ¡Listo!

Si completaste todos los pasos, estás listo para comenzar tu viaje en el desarrollo de IA con Llama.

**¿Qué sigue?**

👉 [Ve al Capítulo 0](docs/01-capitulo-0.md) para comenzar el aprendizaje formal

👉 [Explora los ejemplos](code/) para ver código en acción

👉 [Únete a la comunidad](community/) para conectar con otros desarrolladores

---

**¿Necesitas ayuda?** No dudes en [abrir un issue](https://github.com/majorjuanjo/llama/issues/new/choose)

**¡Feliz aprendizaje!** 🚀
