# Capítulo 2: Configuración del Entorno

## 📖 Contenido

1. [Instalación de Ollama](#instalación-de-ollama)
2. [Descarga de Modelos](#descarga-de-modelos)
3. [Configuración de Python](#configuración-de-python)
4. [Herramientas de Desarrollo](#herramientas-de-desarrollo)
5. [Verificación de la Instalación](#verificación-de-la-instalación)

---

## Instalación de Ollama

Ollama es la forma más sencilla de ejecutar Llama y otros LLMs localmente.

### Windows

```bash
# Descarga el instalador desde ollama.ai
# O usa winget
winget install Ollama.Ollama
```

### macOS

```bash
# Descarga desde ollama.ai
# O usa Homebrew
brew install ollama
```

### Linux

```bash
# Instalación con script oficial
curl -fsSL https://ollama.ai/install.sh | sh

# O instalación manual
# Descarga desde GitHub releases
wget https://github.com/ollama/ollama/releases/latest/download/ollama-linux-amd64
sudo install -o0 -g0 -m755 ollama-linux-amd64 /usr/local/bin/ollama
```

### Verificación de Ollama

```bash
# Verifica la instalación
ollama --version

# Inicia el servicio (si no se inició automáticamente)
ollama serve
```

## Descarga de Modelos

### Modelos Llama Recomendados

```bash
# Modelo pequeño para comenzar (1B parámetros)
ollama pull llama3.2:1b

# Modelo medio, buen balance (3B parámetros)
ollama pull llama3.2:3b

# Modelo estándar (8B parámetros) - RECOMENDADO
ollama pull llama3.1:8b

# Modelo grande para tareas complejas (70B parámetros)
ollama pull llama3.1:70b
```

### Lista de Modelos Disponibles

```bash
# Ver modelos instalados
ollama list

# Buscar modelos disponibles
ollama search llama

# Ver información de un modelo
ollama show llama3.1:8b
```

### Espacio en Disco Requerido

| Modelo | Cuantización | Tamaño Aprox. |
|--------|--------------|---------------|
| llama3.2:1b | Q4 | ~1GB |
| llama3.2:3b | Q4 | ~2GB |
| llama3.1:8b | Q4 | ~4.7GB |
| llama3.1:8b | Q8 | ~8.5GB |
| llama3.1:70b | Q4 | ~40GB |

## Configuración de Python

### Instalación de Python

```bash
# Verifica si Python está instalado
python --version
# o
python3 --version

# Debe ser Python 3.8 o superior
```

### Entorno Virtual

```bash
# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### Instalación de Dependencias

```bash
# Actualiza pip
pip install --upgrade pip

# Instala bibliotecas esenciales
pip install ollama
pip install langchain
pip install langchain-community
pip install chromadb
pip install sentence-transformers
pip install requests
pip install python-dotenv
```

### Archivo requirements.txt

Crea un archivo `requirements.txt`:

```txt
ollama>=0.1.0
langchain>=0.1.0
langchain-community>=0.0.20
chromadb>=0.4.0
sentence-transformers>=2.3.0
requests>=2.31.0
python-dotenv>=1.0.0
fastapi>=0.109.0
uvicorn>=0.27.0
```

Instala con:
```bash
pip install -r requirements.txt
```

## Herramientas de Desarrollo

### Editor de Código

Recomendaciones:
- **VS Code**: Con extensiones Python, Jupyter
- **PyCharm**: Edición Community gratuita
- **Cursor**: AI-powered IDE

### VS Code - Extensiones Recomendadas

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "github.copilot",
    "esbenp.prettier-vscode"
  ]
}
```

### Git (Opcional pero Recomendado)

```bash
# Verifica instalación
git --version

# Configura tu identidad
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Docker (Opcional)

Para despliegues y aislamiento:

```bash
# Verifica instalación
docker --version

# Imagen básica con Ollama
docker pull ollama/ollama
```

## Verificación de la Instalación

### Test 1: Ollama CLI

```bash
# Prueba rápida de generación
ollama run llama3.2:1b "¿Cuál es la capital de México?"

# Debe responder: "La capital de México es Ciudad de México..."
```

### Test 2: Python + Ollama

Crea `test_ollama.py`:

```python
import ollama

# Test básico
response = ollama.chat(
    model='llama3.2:1b',
    messages=[{
        'role': 'user',
        'content': '¿Cuál es la capital de México?'
    }]
)

print(response['message']['content'])
```

Ejecuta:
```bash
python test_ollama.py
```

### Test 3: Servidor API

```bash
# En una terminal, inicia Ollama
ollama serve

# En otra terminal, prueba la API
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "¿Cuál es la capital de México?",
  "stream": false
}'
```

### Test 4: Recursos del Sistema

```python
# test_resources.py
import psutil
import platform

print(f"Sistema Operativo: {platform.system()}")
print(f"CPU: {platform.processor()}")
print(f"Núcleos CPU: {psutil.cpu_count()}")
print(f"RAM Total: {psutil.virtual_memory().total / (1024**3):.2f} GB")
print(f"RAM Disponible: {psutil.virtual_memory().available / (1024**3):.2f} GB")

# Agrega a requirements.txt: psutil
```

## Solución de Problemas Comunes

### Problema: "Ollama not found"

```bash
# Verifica que Ollama esté en el PATH
echo $PATH  # macOS/Linux
echo %PATH%  # Windows

# Reinicia la terminal después de instalar
```

### Problema: "Out of Memory"

```bash
# Usa un modelo más pequeño
ollama pull llama3.2:1b

# O aumenta swap en Linux
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Problema: "Connection refused"

```bash
# Asegúrate de que Ollama esté ejecutándose
ollama serve

# Verifica el puerto
lsof -i :11434  # macOS/Linux
netstat -ano | findstr :11434  # Windows
```

## 🎯 Ejercicio Práctico

1. **Instalación Completa**:
   - Instala Ollama
   - Descarga al menos 2 modelos diferentes
   - Configura un entorno virtual Python
   - Instala todas las dependencias

2. **Prueba de Rendimiento**:
   - Mide el tiempo de respuesta de diferentes modelos
   - Compara cuantizaciones (Q4 vs Q8)

3. **Script de Verificación**:
   - Crea un script que verifique todas las dependencias
   - Debe mostrar versiones y confirmar que todo funciona

---

## 📚 Recursos de Instalación

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Python Official](https://www.python.org/)
- [Docker Documentation](https://docs.docker.com/)

## ➡️ Siguiente Paso

Continúa con el [Capítulo 3: Construcción de Aplicaciones](./04-capitulo-3.md) para crear tu primera aplicación.
