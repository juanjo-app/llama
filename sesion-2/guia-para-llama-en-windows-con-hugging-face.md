# Guia para Llama en Windows con Hugging Face

### PARTE 1: DIAGNÓSTICO SYSTEM AVANZADO

{% stepper %}
{% step %}
#### Detectar Hardware&#x20;

Script Python: Diagnóstico completo

```python
import torch
import subprocess
import psutil
import os
from pathlib import Path

def diagnose_system():
    """Diagnóstico completo Windows + PyTorch"""
    
    print("=" * 60)
    print("DIAGNÓSTICO SISTEMA - LLAMA LOCAL")
    print("=" * 60)
    
    # 1. CPU
    print("\n📊 CPU")
    print(f"  Cores físicos: {psutil.cpu_count(logical=False)}")
    print(f"  Threads lógicos: {psutil.cpu_count(logical=True)}")
    print(f"  Frecuencia: {psutil.cpu_freq().current:.1f} MHz")
    
    # 2. RAM
    print("\n💾 MEMORIA")
    ram = psutil.virtual_memory()
    print(f"  Total: {ram.total / (1024**3):.1f} GB")
    print(f"  Disponible: {ram.available / (1024**3):.1f} GB")
    print(f"  Uso: {ram.percent}%")
    
    # 3. Disco
    print("\n💿 ALMACENAMIENTO")
    disk = psutil.disk_usage('/')
    print(f"  Total: {disk.total / (1024**3):.1f} GB")
    print(f"  Libre: {disk.free / (1024**3):.1f} GB")
    print(f"  Uso: {disk.percent}%")
    
    # 4. GPU
    print("\n🎮 GPU")
    if torch.cuda.is_available():
        print(f"  ✓ CUDA disponible")
        print(f"  Device: {torch.cuda.get_device_name(0)}")
        print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.1f} GB")
        print(f"  VRAM disponible: {torch.cuda.mem_get_info()[0] / (1024**3):.1f} GB")
        print(f"  CUDA version: {torch.version.cuda}")
        print(f"  cuDNN version: {torch.backends.cudnn.version()}")
    else:
        print(f"  ✗ CUDA NO disponible (CPU only)")
    
    # 5. PyTorch
    print("\n⚙️ PYTORCH")
    print(f"  Version: {torch.__version__}")
    print(f"  Backend: {'CUDA' if torch.cuda.is_available() else 'CPU'}")
    
    # 6. Python
    print("\n🐍 PYTHON")
    print(f"  Version: {os.sys.version.split()[0]}")
    print(f"  Ejecutable: {os.sys.executable}")
    
    # 7. Recomendación
    print("\n🎯 RECOMENDACIÓN")
    ram_gb = ram.total / (1024**3)
    
    if torch.cuda.is_available():
        vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f"  ✓ GPU disponible ({vram_gb:.1f} GB VRAM)")
        
        if vram_gb >= 24:
            print(f"  → Usa: Llama-3.1-70B-Instruct (sin quantización)")
        elif vram_gb >= 16:
            print(f"  → Usa: Llama-3.1-70B-Instruct (q4_0)")
        elif vram_gb >= 8:
            print(f"  → Usa: Llama-3.1-8B-Instruct (sin quantización)")
        else:
            print(f"  → Usa: Llama-3.1-8B-Instruct (q4_0)")
    else:
        print(f"  ✗ GPU NO disponible (CPU only)")
        
        if ram_gb >= 32:
            print(f"  → Usa: Llama-3.1-8B-Instruct (q5_0)")
        elif ram_gb >= 16:
            print(f"  → Usa: Llama-3.1-8B-Instruct (q4_0)")
        else:
            print(f"  → Usa: Llama-3.1-3B-Instruct (q4_0)")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    diagnose_system()
```

Ejecutar:

```bash
python diagnose.py
```
{% endstep %}

{% step %}
#### Matriz de Recomendaciones&#x20;

| RAM  | GPU VRAM | Setup    | Modelo Recomendado  | Latencia |
| ---- | -------- | -------- | ------------------- | -------- |
| 8GB  | 0        | CPU only | Llama 3.1 3B q4\_0  | 5-10s    |
| 16GB | 0        | CPU only | Llama 3.1 8B q4\_0  | 2-5s     |
| 32GB | 0        | CPU only | Llama 3.1 8B q5\_0  | 1-3s     |
| 16GB | 8GB      | GPU      | Llama 3.1 8B fp16   | 1-2s     |
| 32GB | 16GB     | GPU      | Llama 3.1 70B q4\_0 | 0.5-1s   |
| 64GB | 24GB     | GPU      | Llama 3.1 70B fp16  | 0.3-0.5s |
{% endstep %}
{% endstepper %}

***

## PARTE 2: SETUP ENVIRONMENT AVANZADO

### Virtual Environment Management&#x20;

{% tabs %}
{% tab title="venv (Recomendado)" %}
```bash
# Crear environment específico para Llama
python -m venv llama-env

# Activar
llama-env\Scripts\activate  # Windows

# Verificar
python --version
pip --version
```
{% endtab %}

{% tab title="Miniconda (Para GPU/CUDA)" %}
```bash
# Descargar Miniconda desde https://docs.conda.io/projects/miniconda/

# Crear environment
conda create -n llama python=3.11 -y

# Activar
conda activate llama

# Instalar CUDA + cuDNN (si GPU NVIDIA)
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```
{% endtab %}

{% tab title="WSL2 + Linux (Avanzado)" %}
```bash
# En WSL2 (Ubuntu dentro Windows)
wsl --install

# Dentro WSL:
python -m venv llama-env
source llama-env/bin/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
{% endtab %}
{% endtabs %}

### Paso 2.2: Instalar Dependencias&#x20;

Script de instalación completo:

```bash
# 1. Actualizar pip
python -m pip install --upgrade pip setuptools wheel

# 2. PyTorch (CPU o GPU)

# GPU NVIDIA:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# GPU AMD (ROCm):

# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7

# CPU only:

# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 3. Transformers + dependencias
pip install transformers accelerate safetensors

# 4. Herramientas adicionales
pip install huggingface-hub datasets tokenizers

# 5. Para optimización
pip install bitsandbytes  # Quantización
pip install peft          # Parameter-efficient fine-tuning
pip install trl           # Reinforcement Learning

# 6. Para API/Deployment
pip install fastapi uvicorn pydantic

# 7. Para monitoreo
pip install psutil py-cpuinfo

# 8. Verificar instalación
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}')"
```

***

## PARTE 3: DESCARGA INTELIGENTE DE MODELOS

### Autenticación Hugging Face



```python
from huggingface_hub import login, list_repo_files
import os

def setup_hf_auth():
    """Setup HF authentication"""
    
    # Opción 1: Token desde archivo
    token_file = os.path.expanduser("~/.hf_token")
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token = f.read().strip()
        login(token=token, add_to_git_credential=True)
        print("✓ Autenticación desde archivo")
        return
    
    # Opción 2: Variable entorno
    if "HF_TOKEN" in os.environ:
        token = os.environ["HF_TOKEN"]
        login(token=token)
        print("✓ Autenticación desde variable entorno")
        return
    
    # Opción 3: Interactivo
    print("Ingresa token HF (obtén en https://huggingface.co/settings/tokens):")
    token = input("Token: ").strip()
    
    if token:
        login(token=token, add_to_git_credential=True)
        
        # Guardar para próximas veces
        save = input("¿Guardar token para próximas veces? (s/n): ").lower()
        if save == 's':
            os.makedirs(os.path.dirname(token_file), exist_ok=True)
            with open(token_file, 'w') as f:
                f.write(token)
            os.chmod(token_file, 0o600)  # Solo lectura usuario
        
        print("✓ Autenticación exitosa")
    else:
        print("⚠️ No se proporcionó token")

if __name__ == "__main__":
    setup_hf_auth()
```

### Descarga con Resume Automático

```python
from huggingface_hub import snapshot_download
from pathlib import Path
import torch

def download_model_smart(model_id: str, use_quantization=False):
    """
    Descarga modelo con:
    - Resume automático
    - Validación integridad
    - Selección quantización automática
    - Progreso detallado
    """
    
    print(f"Descargando {model_id}...")
    
    # Directorio caché
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    # Detectar si usar quantización
    if use_quantization and not torch.cuda.is_available():
        print("⚠️ GPU no disponible, usando quantización recomendada")
        model_id_actual = model_id.replace("-Instruct", "-Instruct-q4_0")
    else:
        model_id_actual = model_id
    
    try:
        # Descargar con resume
        model_path = snapshot_download(
            repo_id=model_id_actual,
            cache_dir=str(cache_dir),
            resume_download=True,
            local_dir_use_symlinks=False,
            allow_patterns=["*.safetensors", "*.json", "*.txt"],
            ignore_patterns=["*.msgpack", "*.h5"],
        )
        
        print(f"✓ Modelo descargado en: {model_path}")
        
        # Validar integridad
        print("Validando integridad...")
        required_files = [
            "config.json",
            "generation_config.json",
            "model.safetensors" or "pytorch_model.bin"
        ]
        
        for file in required_files:
            if not (Path(model_path) / file).exists():
                print(f"⚠️ Archivo faltante: {file}")
        
        print("✓ Validación completada")
        return model_path
        
    except Exception as e:
        print(f"✗ Error descarga: {e}")
        return None

if __name__ == "__main__":
    path = download_model_smart(
        "meta-llama/Llama-3.1-8B-Instruct",
        use_quantization=False
    )
```

***

## PARTE 4: INFERENCE OPTIMIZADO&#x20;

### Pipeline&#x20;

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import time

class LlamaOptimizedPipeline:
    """Pipeline Llama con optimizaciones avanzadas"""
    
    def __init__(self, model_id: str = "meta-llama/Llama-3.1-8B-Instruct", 
                 quantization=None, device="auto"):
        
        print(f"Cargando modelo: {model_id}")
        start = time.time()
        
        # Seleccionar dtype según hardware
        if torch.cuda.is_available():
            dtype = torch.float16 if torch.cuda.get_device_properties(0).total_memory < 16 * 1024**3 else torch.bfloat16
        else:
            dtype = torch.float32
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=dtype,
            device_map=device,
            load_in_4bit=quantization == "int4",
            load_in_8bit=quantization == "int8",
        )
        
        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            torch_dtype=dtype,
            device_map=device,
        )
        
        elapsed = time.time() - start
        print(f"✓ Modelo cargado en {elapsed:.1f}s")
    
    def generate(self, prompt: str, max_length=512, temperature=0.7) -> dict:
        """Generar texto con feedback detallado"""
        
        start = time.time()
        
        sequences = self.pipeline(
            prompt,
            do_sample=True,
            top_p=0.9,
            top_k=50,
            temperature=temperature,
            num_return_sequences=1,
            max_length=max_length,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        
        elapsed = time.time() - start
        
        return {
            "prompt": prompt,
            "response": sequences[0]['generated_text'],
            "time_seconds": elapsed,
            "model": self.model.config.model_type,
            "dtype": str(self.model.dtype)
        }

# Uso
llama = LlamaOptimizedPipeline()
result = llama.generate("¿Qué es IA?")
print(result["response"])
print(f"Tiempo: {result['time_seconds']:.2f}s")
```

***

## PARTE 5: CHAT CONVERSACIONAL AVANZADO

### Chat Multi-Turno con Contexto

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LlamaChatbot:
    """Chatbot conversacional con historial persistente"""
    
    def __init__(self, model_id="meta-llama/Llama-3.1-8B-Instruct"):
        print(f"Inicializando chatbot...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto",
        )
        
        self.conversation_history = []
        self.system_prompt = "Eres un asistente IA amable y útil."
    
    def format_conversation(self):
        """Formatear historial para Llama"""
        prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{self.system_prompt}<|eot_id|>"
        
        for message in self.conversation_history:
            role = message["role"]
            content = message["content"]
            prompt += f"<|start_header_id|>{role}<|end_header_id|>\n\n{content}<|eot_id|>"
        
        prompt += "<|start_header_id|>assistant<|end_header_id|>\n\n"
        return prompt
    
    def chat(self, user_message: str, max_new_tokens=256) -> str:
        """Enviar mensaje y obtener respuesta"""
        
        # Agregar a historial
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Formatear prompt
        prompt = self.format_conversation()
        
        # Tokenizar
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        
        # Generar
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        
        # Decodificar
        response = self.tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        
        # Guardar en historial
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response
    
    def clear_history(self):
        """Limpiar conversación"""
        self.conversation_history = []
    
    def set_system_prompt(self, prompt: str):
        """Cambiar system prompt"""
        self.system_prompt = prompt
    
    def save_conversation(self, filename: str):
        """Guardar conversación a archivo"""
        import json
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
        print(f"Conversación guardada en {filename}")
    
    def load_conversation(self, filename: str):
        """Cargar conversación desde archivo"""
        import json
        with open(filename, 'r') as f:
            self.conversation_history = json.load(f)
        print(f"Conversación cargada desde {filename}")

# Uso
bot = LlamaChatbot()
bot.set_system_prompt("Eres experto en normativa mexicana de IA (LFPDPPP). Responde en Spanish.")

print(bot.chat("¿Qué es LFPDPPP?"))
print(bot.chat("¿Cuáles son mis obligaciones como MiPyME?"))  # Mantiene contexto
print(bot.chat("¿Penalidades?"))

bot.save_conversation("chat_compliance.json")
```

***

## PARTE 6: API REST PRODUCTION-READY

### FastAPI + Transformers

```python
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json
import time
from datetime import datetime

app = FastAPI(
    title="Llama API - Local Inference",
    description="API para Llama local con Transformers"
)

# Carga modelo al iniciar
@app.on_event("startup")
async def load_model():
    global model, tokenizer
    print("Cargando modelo...")
    model_id = "meta-llama/Llama-3.1-8B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
    )
    print("✓ Modelo cargado")

# Modelos Pydantic
class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 512
    temperature: float = 0.7
    top_p: float = 0.9

class GenerateResponse(BaseModel):
    prompt: str
    response: str
    tokens: int
    time_seconds: float
    timestamp: str

# Endpoints
@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """Generar texto"""
    try:
        start = time.time()
        
        inputs = tokenizer(request.prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=request.max_length,
                temperature=request.temperature,
                top_p=request.top_p,
                do_sample=True,
            )
        
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        elapsed = time.time() - start
        
        return GenerateResponse(
            prompt=request.prompt,
            response=response,
            tokens=outputs.shape[1] - inputs['input_ids'].shape[1],
            time_seconds=elapsed,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "ok",
        "model_loaded": True,
        "device": str(model.device),
        "dtype": str(model.dtype)
    }

@app.get("/info")
async def info():
    """Info del modelo"""
    return {
        "model": model.config.model_type,
        "parameters": model.config.num_parameters,
        "hidden_size": model.config.hidden_size,
        "max_position_embeddings": model.config.max_position_embeddings,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
```

Ejecutar:

```bash
pip install fastapi uvicorn
python api.py

# Test
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "¿Qué es IA?", "max_length": 256}'
```

***

## PARTE 7: MONITOREO GPU EN TIEMPO REAL

### Monitor GPU + RAM

```python
import torch
import psutil
import subprocess
import threading
import time
from datetime import datetime

class GPUMonitor:
    """Monitoreo GPU NVIDIA en tiempo real"""
    
    def __init__(self, update_interval=1):
        self.update_interval = update_interval
        self.running = False
        self.metrics = {}
    
    def get_nvidia_stats(self):
        """Obtener stats NVIDIA-SMI"""
        try:
            result = subprocess.run(
                [
                    'nvidia-smi',
                    '--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free,temperature.gpu,utilization.gpu,utilization.memory',
                    '--format=csv,noheader'
                ],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                return result.stdout.strip()
            return None
        except:
            return None
    
    def get_pytorch_memory(self):
        """Obtener memoria PyTorch"""
        if torch.cuda.is_available():
            allocated = torch.cuda.memory_allocated() / (1024**3)
            reserved = torch.cuda.memory_reserved() / (1024**3)
            return {
                "allocated_gb": allocated,
                "reserved_gb": reserved,
                "free_mb": (torch.cuda.get_device_properties(0).total_memory - torch.cuda.memory_allocated()) / (1024**2)
            }
        return None
    
    def monitor_loop(self):
        """Loop de monitoreo"""
        print("Iniciando monitoreo GPU...")
        print("Presiona Ctrl+C para salir\n")
        
        while self.running:
            self.metrics['timestamp'] = datetime.now().isoformat()
            
            # CPU/RAM sistema
            cpu_percent = psutil.cpu_percent(interval=0.5)
            ram = psutil.virtual_memory()
            
            # GPU
            nvidia_stats = self.get_nvidia_stats()
            pytorch_mem = self.get_pytorch_memory()
            
            # Print
            print(f"\n[{self.metrics['timestamp']}]")
            print(f"System - CPU: {cpu_percent}% | RAM: {ram.percent}% ({ram.used / (1024**3):.1f}GB / {ram.total / (1024**3):.1f}GB)")
            
            if nvidia_stats:
                print(f"GPU Stats:\n{nvidia_stats}")
            
            if pytorch_mem:
                print(f"PyTorch - Allocated: {pytorch_mem['allocated_gb']:.1f}GB | Reserved: {pytorch_mem['reserved_gb']:.1f}GB")
            
            time.sleep(self.update_interval)
    
    def start(self):
        """Iniciar monitoreo en background"""
        self.running = True
        thread = threading.Thread(target=self.monitor_loop, daemon=True)
        thread.start()
    
    def stop(self):
        """Detener monitoreo"""
        self.running = False

if __name__ == "__main__":
    monitor = GPUMonitor()
    monitor.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
        print("\nMonitoreo detenido")
```

***

## PARTE 8: CUANTIZACIÓN Y OPTIMIZACIÓN

### Cargar modelo con Cuantización

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

def load_model_quantized(model_id: str, quantization: str = "int8"):
    """
    Cargar modelo con quantización:
    - int8: Máxima compresión, menor precisión
    - int4: Máxima compresión, mucho menor precisión
    - bfloat16: Sin quantización, pero precisión reducida
    """
    
    print(f"Cargando {model_id} con {quantization}...")
    
    if quantization == "int8":
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            load_in_8bit=True,
            device_map="auto",
            torch_dtype=torch.float16,
        )
    
    elif quantization == "int4":
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=bnb_config,
            device_map="auto",
        )
    
    elif quantization == "bfloat16":
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )
    
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto",
        )
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    print(f"✓ Modelo cargado con {quantization}")
    
    # Estimar memoria
    param_count = model.num_parameters
    param_size_gb = (param_count * 2) / (1024**3)  # Estimación
    print(f"Parámetros: {param_count / 1e9:.1f}B")
    print(f"RAM estimado: {param_size_gb:.1f}GB")
    
    return model, tokenizer

# Uso
model, tokenizer = load_model_quantized(
    "meta-llama/Llama-3.1-8B-Instruct",
    quantization="int4"  # Para GPU con < 8GB VRAM
)
```

***

## PARTE 9: COMPLIANCE LFPDPPP&#x20;

## Data Protection Framework

```python
import hashlib
import json
from datetime import datetime
from pathlib import Path

class LlamaComplianceManager:
    """Gestor compliance LFPDPPP para Llama local"""
    
    def __init__(self, log_dir="compliance_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
    
    def detect_pii(self, text: str) -> list:
        """Detectar información personal en texto"""
        import re
        
        detections = []
        
        # Emails
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        if emails:
            detections.append({"type": "email", "count": len(emails)})
        
        # RFC México
        rfcs = re.findall(r'\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b', text)
        if rfcs:
            detections.append({"type": "rfc", "count": len(rfcs)})
        
        # Teléfonos
        phones = re.findall(r'\b\d{10}\b|\+\d{1,3}\s*\d+', text)
        if phones:
            detections.append({"type": "phone", "count": len(phones)})
        
        # Números de cuenta/tarjeta
        cards = re.findall(r'\b\d{13,19}\b', text)
        if cards:
            detections.append({"type": "card", "count": len(cards)})
        
        return detections
    
    def log_interaction(self, user_input: str, model_output: str, pii_detected: list):
        """Registrar interacción con compliance"""
        
        # Detectar PII
        pii_in_input = self.detect_pii(user_input)
        pii_in_output = self.detect_pii(model_output)
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input_hash": hashlib.sha256(user_input.encode()).hexdigest(),
            "model_output_hash": hashlib.sha256(model_output.encode()).hexdigest(),
            "pii_detected": {
                "input": pii_in_input,
                "output": pii_in_output
            },
            "action_taken": "FLAGGED" if (pii_in_input or pii_in_output) else "ALLOWED"
        }
        
        # Guardar log
        log_file = self.log_dir / f"llama_compliance_{datetime.now().strftime('%Y%m%d')}.jsonl"
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")
        
        return log_entry
    
    def generate_compliance_report(self):
        """Generar reporte compliance"""
        
        total_interactions = 0
        pii_detections = 0
        
        for log_file in self.log_dir.glob("*.jsonl"):
            with open(log_file) as f:
                for line in f:
                    total_interactions += 1
                    entry = json.loads(line)
                    if entry['pii_detected']['input'] or entry['pii_detected']['output']:
                        pii_detections += 1
        
        report = {
            "date": datetime.now().isoformat(),
            "total_interactions": total_interactions,
            "pii_detections": pii_detections,
            "compliance_rate": (1 - pii_detections / max(total_interactions, 1)) * 100,
            "recommendations": [
                "Implementar ofuscación de PII",
                "Revisar datos de entrenamiento",
                "Auditar logs regularmente",
                "Encriptar almacenamiento local"
            ]
        }
        
        return report

# Uso
compliance = LlamaComplianceManager()

# En cada request
user_msg = "Mi email es juan@example.com y RFC es ABCD123456XYZ"
model_out = "Recibido correctamente"

log = compliance.log_interaction(user_msg, model_out, [])
print(f"Log: {log['action_taken']}")

# Reporte mensual
report = compliance.generate_compliance_report()
print(json.dumps(report, indent=2))
```

***

## PARTE 10: CASOS PRÁCTICOS MIPYMES

### Caso: Asistente Legal Compliance

```python
class LlamaLegalAssistant:
    """Asistente legal especializado en normativa mexicana"""
    
    LEGAL_SYSTEM_PROMPT = """
    Eres abogado especializado en derecho digital mexicano.
    
    Área de expertise:
    - LFPDPPP (Protección datos personales)
    - Código Penal (Delitos informáticos art. 211 bis)
    - LFCE (Competencia económica)
    - LFDA (Derechos autor - SCJN 2025 precedente IA)
    - Ley Olimpia (Deepfakes)
    - NOM-151 (Conservación datos)
    - CNPP (Responsabilidad corporativa)
    
    Para cada pregunta:
    1. Cita artículos específicos
    2. Explica obligación MiPyME
    3. Da caso práctico aplicable
    4. Sugiere acciones legales
    5. Advierta penalidades máximas
    
    Responde en Spanish, sé preciso.
    Si no sabes exactamente, di "Requiere asesoramiento legal profesional".
    """
    
    def __init__(self, model):
        self.model = model
        self.tokenizer = model.tokenizer
    
    def get_legal_advice(self, question: str) -> str:
        """Obtener asesoramiento legal"""
        
        prompt = f"""[INST] {self.LEGAL_SYSTEM_PROMPT}

Pregunta del usuario: {question} [/INST]"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.model.device)
        
        with torch.no_grad():
            outputs = self.model.model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.3,  # Bajo para precisión
            )
        
        response = self.tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        return response

# Uso

# legal_bot = LlamaLegalAssistant(llama)

# print(legal_bot.get_legal_advice("¿Cómo cumplir LFPDPPP si uso IA en RRHH?"))
```

***

## PARTE 11: FINE-TUNING FRAMEWORK

### LoRA Fine-tuning

```python
from peft import get_peft_model, LoraConfig, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def setup_lora_model(model_id: str, rank: int = 8):
    """Configurar modelo para LoRA fine-tuning"""
    
    # Modelo base
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    
    # Configuración LoRA
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=rank,  # Rank bajo = menos parámetros entrenables
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        target_modules=["q_proj", "v_proj"]  # Módulos a entrenar
    )
    
    # Aplicar LoRA
    model = get_peft_model(model, peft_config)
    
    # Resumen
    print(model.print_trainable_parameters())
    
    return model

# Uso

# model = setup_lora_model("meta-llama/Llama-3.1-8B-Instruct")

# # Ahora entrenar con tus datos...
```

***

## PARTE 12: DEPLOYMENT DOCKER

### Dockerfile

```dockerfile
FROM nvidia/cuda:12.1-cudnn8-runtime-ubuntu22.04

WORKDIR /app

# Instalar Python
RUN apt-get update && apt-get install -y python3.11 python3.11-venv python3.11-dev

# Crear venv
RUN python3.11 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar código
COPY . .

# Exponir puerto
EXPOSE 8000

# Start
CMD ["python", "api.py"]
```

requirements.txt:

```
torch==2.1.0
transformers==4.35.0
fastapi==0.104.0
uvicorn==0.24.0
accelerate==0.24.0
huggingface-hub==0.17.0
peft==0.7.0
```

Build & Run:

```bash
docker build -t llama-api .
docker run --gpus all -p 8000:8000 llama-api
```

***

## PARTE 13-15: TROUBLESHOOTING, BENCHMARKING, ROADMAP

A continuación se resume lo esencial. Para detalles extensos, consulte los scripts en cada sección y los logs generados en su instalación.

<details>

<summary>Troubleshooting Común</summary>

* CUDA out of memory → Usar quantización, reducir batch size, usar offloading o 4bit/8bit.
* Modelo no se descarga → Verificar token HF, espacio en disco, usar resume automático.
* API lenta → Optimizar batch size, usar workers/uvicorn tuning, caching de tokenización.
* GPU no detectada → Revisar drivers, CUDA toolkit, PATH, reiniciar máquina/WSL, verificar nvidia-smi.
* Problemas con bitsandbytes en Windows → Usar WSL2 o contenedores Linux con CUDA.
* Error de mismatched dtype → Asegurar torch\_dtype consistente en carga y generación.
* Permisos de archivo en token guardado → Revisar chmod 600 para \~/.hf\_token.
* Incompatibilidades entre versiones de transformers/accelerate → Alinear versiones en requirements.txt.

</details>

<details>

<summary>Benchmarking</summary>

* Implementar mediciones de tokens/segundo y latencia por petición.
* Comparar modelos (3B, 8B, 70B) con y sin quantización.
* Registrar GPU utilizations y p99/p95 latencies.
* Automatizar benchmarks con scripts que ejecuten múltiples prompts y guarden resultados en CSV/JSON.

</details>

<details>

<summary>Roadmap 6 Semanas</summary>

* Semana 1: Setup + diagnóstico
* Semana 2: Inference básico
* Semana 3: API REST
* Semana 4: Optimization
* Semana 5: Fine-tuning
* Semana 6: Production deployment

</details>

***

## CONCLUSIÓN: Repaso en guía

<table><thead><tr><th width="298">Aspecto</th><th>Esta Guía</th></tr></thead><tbody><tr><td>Pasos</td><td>15 secciones</td></tr><tr><td>Hardware detect</td><td>✅ Automático</td></tr><tr><td>Descarga resume</td><td>✅ Sí</td></tr><tr><td>Optimization</td><td>✅ Quantización + bfloat16</td></tr><tr><td>API REST</td><td>✅ FastAPI production</td></tr><tr><td>GPU monitor</td><td>✅ Real-time</td></tr><tr><td>Compliance LFPDPPP</td><td>✅ Framework</td></tr><tr><td>Fine-tuning</td><td>✅ LoRA setup</td></tr><tr><td>Docker</td><td>✅ Dockerfile</td></tr><tr><td>Troubleshooting</td><td>✅ 8+ problemas</td></tr><tr><td>Casos prácticos</td><td>✅ 3+ MiPyMEs</td></tr></tbody></table>

***
