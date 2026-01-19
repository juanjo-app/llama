# Macrotabla de decisiones

### Base de Datos Interactiva para Navegar

## ESTRUCTURA AIRTABLE

### TABLA 1: DECISIONES INICIALES (START HERE)

| Campo                       | Tipo            | Descripción          |
| --------------------------- | --------------- | -------------------- |
| **Pregunta**                | Text            | Pregunta del usuario |
| **Respuesta Corta**         | Text            | Respuesta en 1 línea |
| **Documentos Relacionados** | Link to Records | Guías aplicables     |
| **Tiempo de lectura**       | Number          | Minutos recomendados |
| **Prioridad**               | Select          | High/Medium/Low      |

#### DECISIONES MAPEO

```
DECISIÓN 1: "¿LOCAL O CLOUD?"
├─ Local (Tengo GPU/Mac/Linux)
│  ├─ LM Studio [172]
│  ├─ Ollama Mac [173]
│  └─ HF Transformers [174]
└─ Cloud (Quiero 24/7 uptime)
   ├─ AWS Bedrock [175]
   └─ Llama 4 Cloud (esperado 2026) [176]

DECISIÓN 2: "¿CUÁNTA COMPLEJIDAD?"
├─ Principiante (chat simple)
│  └─ LM Studio [172] → 30 min
├─ Intermedio (análisis legal)
│  └─ HF Transformers [174] → 2 horas
└─ Avanzado (production API)
   └─ AWS Bedrock [175] → 4 horas

DECISIÓN 3: "¿NECESITO COMPLIANCE?"
├─ No (solo experimentation)
│  └─ Cualquier guía local
├─ Sí, básico (LFPDPPP awareness)
│  └─ Sección E: Glosario [178]
└─ Sí, full (auditoría completa)
   └─ AWS Bedrock [175] + Glosario [178]

DECISIÓN 4: "¿NECESITO FINE-TUNING?"
├─ No (usar modelo base)
│  └─ Cualquier guía
├─ Sí, LoRA (eficiente)
│  └─ Sección III Meta Conglomerada [177]
└─ Sí, Full (máxima calidad)
   └─ Sección III Meta Conglomerada [177]

DECISIÓN 5: "¿NECESITO OPTIMIZACIÓN?"
├─ No (latencia no crítica)
│  └─ Cualquier guía
├─ Sí, quantización
│  └─ Sección IV Meta Conglomerada [177]
└─ Sí, distillation
   └─ Sección IV Meta Conglomerada [177]
```

***

### TABLA 2: MATRIZ GUÍAS (TODOS LOS DOCUMENTOS)

| Guía ID | Nombre                  | Páginas | Secciones    | Best For                      | Time    | URL    |
| ------- | ----------------------- | ------- | ------------ | ----------------------------- | ------- | ------ |
| **167** | Módulo Integral GitBook | 50      | 5            | Currículum base               | 2h      | \[167] |
| **169** | Estrategia Despliegue   | 40      | 6            | Arquitectura                  | 1.5h    | \[169] |
| **170** | Obsidian Wikipedia      | 50      | 12           | Wiki structure                | 2h      | \[170] |
| **171** | AWS Bedrock v1          | 60      | 10           | Cloud basics                  | 2.5h    | \[171] |
| **172** | LM Studio               | 70      | 10           | GUI fácil                     | 2.5h    | \[172] |
| **173** | Ollama Mac              | 70      | 12           | Terminal Mac                  | 2.5h    | \[173] |
| **174** | HF Transformers         | 80      | 15           | Python production             | 3h      | \[174] |
| **175** | AWS Bedrock SUPERIOR    | 100     | 18           | Enterprise                    | 4h      | \[175] |
| **176** | Llama 4 Anticipatoria   | 80      | 17           | Future-ready                  | 3h      | \[176] |
| **177** | META LLAMA CONGLOMERADA | 200     | 7 partes     | Visión + Prompt + Fine-tuning | 6h      | \[177] |
| **178** | GLOSARIO DEFINITIVO     | 100+    | 15 secciones | Reference                     | ongoing | \[178] |

***

### TABLA 3: MATRIX TECNOLOGÍAS

| Tecnología              | Dificultad | Curva Aprendizaje | Costo Setup | Costo/Mes | ROI           | Guía Ref |
| ----------------------- | ---------- | ----------------- | ----------- | --------- | ------------- | -------- |
| **LM Studio**           | Fácil      | 30 min            | $0          | $0        | Alta (local)  | \[172]   |
| **Ollama**              | Fácil      | 30 min            | $0          | $0        | Alta (local)  | \[173]   |
| **Hugging Face Trans.** | Intermedia | 2h                | $0          | $0-100    | Muy alta      | \[174]   |
| **AWS Bedrock**         | Intermedia | 1h                | $100        | $1-10k    | Alta (scale)  | \[175]   |
| **Docker**              | Avanzada   | 4h                | $0          | $0        | Alta (DevOps) | \[174]   |
| **Fine-tuning LoRA**    | Avanzada   | 3h                | $0          | $50-200   | Crítica       | \[177]   |
| **Quantización**        | Avanzada   | 2h                | $0          | $0        | Crítica       | \[177]   |

***

### TABLA 4: ROADMAP 12 SEMANAS

| Semana  | Objetivo                       | Guías                | Horas | Status     |
| ------- | ------------------------------ | -------------------- | ----- | ---------- |
| **1**   | Setup inicial + decisión       | \[172]/\[173]/\[174] | 5     | Start      |
| **2**   | First model running            | \[172]/\[173]/\[174] | 8     | Validate   |
| **3**   | Chat básico funcional          | \[172]/\[173]/\[174] | 6     | Deploy     |
| **4**   | API REST endpoint              | \[174]/\[175]        | 8     | Production |
| **5**   | Monitoring setup               | \[175]/\[177]        | 6     | Observe    |
| **6**   | Data preparation (fine-tuning) | \[177]               | 10    | Prepare    |
| **7-8** | Fine-tuning LoRA               | \[177]               | 16    | Train      |
| **9**   | Optimization (quantization)    | \[177]               | 8     | Optimize   |
| **10**  | Evaluation + testing           | \[177]               | 8     | Validate   |
| **11**  | Production hardening           | \[175]               | 8     | Secure     |
| **12**  | Scale + documentation          | \[175]/\[178]        | 8     | Document   |

***

### TABLA 5: CASOS DE USO POR SECTOR

#### Sector Legal (62)

| Caso                  | Descripción                    | Guías Aplicables     | Stack Recomendado   | ROI  |
| --------------------- | ------------------------------ | -------------------- | ------------------- | ---- |
| **Análisis contrato** | Review + compliance check      | \[174]/\[175]/\[178] | HF Trans. → Bedrock | 300% |
| **Derechos ARCO**     | Automatizar respuestas LFPDPPP | \[175]/\[178]        | Bedrock API         | 250% |
| **Peritaje digital**  | Generar reportes expertos      | \[177]/\[175]        | Fine-tune + Bedrock | 400% |
| **Case law search**   | RAG + jurisprudencia           | \[177]/\[174]        | RAG + HF            | 200% |
| **Drafting**          | Generar documentos             | \[177]/\[172]        | Llama local         | 150% |

#### Sector RRHH (56)

| Caso                   | Descripción           | Guías         | Stack             | ROI  |
| ---------------------- | --------------------- | ------------- | ----------------- | ---- |
| **Resume screening**   | Clasificar candidatos | \[174]/\[175] | HF + Bedrock      | 350% |
| **Capacitación**       | Generar contenido     | \[172]/\[177] | Llama + Fine-tune | 200% |
| **Compliance laboral** | LFPDPPP + derechos    | \[175]/\[178] | Bedrock           | 300% |

#### Sector Salud (62)

| Caso                      | Descripción           | Guías         | Stack       | ROI  |
| ------------------------- | --------------------- | ------------- | ----------- | ---- |
| **Documentación médica**  | NLP en expedientes    | \[174]/\[173] | HF Trans.   | 250% |
| **Regulatory compliance** | NOM-004 + LFPDPPP     | \[175]/\[178] | Bedrock     | 400% |
| **Patient education**     | Explicar tratamientos | \[172]/\[177] | Llama local | 180% |

***

### TABLA 6: PROBLEMAS Y SOLUCIONES

| Problema                  | Síntoma                    | Solución                        | Guía Ref          | Tiempo Fix |
| ------------------------- | -------------------------- | ------------------------------- | ----------------- | ---------- |
| **GPU out of memory**     | "CUDA out of memory" error | Usar quantización int4          | \[177] sección IV | 30 min     |
| **Slow inference**        | Respuesta 5+ segundos      | Batching + caching              | \[177] sección IV | 2h         |
| **Hallucinations**        | Respuestas incorrectas     | Usar RAG + baja temperatura     | \[177] sección II | 1h         |
| **High latency P95**      | 5-10% requests lentos      | Load balancer + scaling         | \[175]            | 4h         |
| **Model not loading**     | "Model not found" error    | Verificar ruta modelo           | \[172]/\[173]     | 15 min     |
| **Compliance violation**  | LFPDPPP risk               | Audit + encryption setup        | \[175]/\[178]     | 8h         |
| **Fine-tune overfitting** | Test accuracy baja         | Early stopping + regularization | \[177]            | 3h         |
| **Cost spiraling**        | $10k/mes (inesperado)      | Token caching + batch           | \[177]            | 2h         |

***

### TABLA 7: CONCEPTOS CLAVE (LINKERS)

| Concepto         | Definición Corta                  | Guías Principales | Sub-conceptos Relacionados           |
| ---------------- | --------------------------------- | ----------------- | ------------------------------------ |
| **RAG**          | Retrieval-Augmented Generation    | \[174]/\[177]     | Vector DB, Embedding, Context        |
| **Fine-tuning**  | Adaptar modelo con tus datos      | \[177]            | LoRA, QLoRA, Epochs, Loss            |
| **Quantización** | Reducir precisión para speed/size | \[177]            | int4, int8, bfloat16                 |
| **Compliance**   | Seguir normas (LFPDPPP)           | \[175]/\[178]     | ARCO, Consentimiento, Audit          |
| **Evaluation**   | Medir calidad modelo              | \[177]            | Benchmarks, Metrics, Testing         |
| **Deployment**   | Poner en producción               | \[175]            | API, Lambda, Scaling                 |
| **Prompting**    | Instruir a Llama                  | \[177]            | CoT, Few-shot, Temperature           |
| **Distillation** | Crear modelo pequeño de grande    | \[177]            | Teacher, Student, Knowledge transfer |

***

### TABLA 8: PERSONA USER → RECOMENDACIONES

#### User Type: "Principiante Tech"

| Aspecto          | Recomendación                                |
| ---------------- | -------------------------------------------- |
| **Hardware**     | Mac (LM Studio) o Laptop Windows             |
| **Guía start**   | \[172] LM Studio (15 min setup)              |
| **Tiempo aprox** | 2-3 horas total primeros pasos               |
| **Stack**        | LM Studio → Bedrock (eventual)               |
| **Cost/mes**     | $0-500 (depende escala)                      |
| **Riesgo**       | Bajo (GUI amigable)                          |
| **Roadmap**      | Semanas 1-3: Learning; Semana 4+: Production |

#### User Type: "Developer Python"

| Aspecto          | Recomendación                               |
| ---------------- | ------------------------------------------- |
| **Hardware**     | GPU recomendada (RTX 4090/A100)             |
| **Guía start**   | \[174] HF Transformers (2h setup)           |
| **Tiempo aprox** | 4-6 horas setup + 40h integración           |
| **Stack**        | HF Transformers → FastAPI → Bedrock         |
| **Cost/mes**     | $200-2k (depende volumen)                   |
| **Riesgo**       | Medio (más control = más responsabilidad)   |
| **Roadmap**      | Semanas 1-6: Development; Semana 7+: Deploy |

#### User Type: "Enterprise Tech Lead"

| Aspecto          | Recomendación                               |
| ---------------- | ------------------------------------------- |
| **Hardware**     | Full cloud (AWS)                            |
| **Guía start**   | \[175] AWS Bedrock SUPERIOR (1h setup)      |
| **Tiempo aprox** | 10-15 horas arquitectura + compliance       |
| **Stack**        | Bedrock → Lambda → API Gateway → CloudFront |
| **Cost/mes**     | $2k-50k+ (escala automática)                |
| **Riesgo**       | Bajo (AWS maneja infraestructura)           |
| **Roadmap**      | Semanas 1-2: Arch; 3-6: MVP; 7+: Scaling    |

***

### TABLA 9: CHECKLISTS TEMÁTICAS

#### Pre-Deploy Checklist

* [ ] ¿Guía correcta elegida? (Tabla 2)
* [ ] ¿Hardware compatible? (Tabla 3)
* [ ] ¿Código testeado localmente?
* [ ] ¿API endpoint funcional?
* [ ] ¿Monitoring activo?
* [ ] ¿Backup data en lugar?
* [ ] ¿Compliance audit completado?
* [ ] ¿Security hardening done?
* [ ] ¿Team trained?
* [ ] ¿Documentation updated?

#### LFPDPPP Compliance Checklist

* [ ] ¿Consentimiento usuario obtenido?
* [ ] ¿Aviso privacidad menciona IA?
* [ ] ¿Datos encriptados en reposo?
* [ ] ¿TLS 1.2+ en tránsito?
* [ ] ¿Derechos ARCO implementados?
* [ ] ¿Audit trail activo?
* [ ] ¿Data retention policy definida?
* [ ] ¿Seguro responsabilidad civil?
* [ ] ¿Responsable de datos designado?
* [ ] ¿Breach notification plan?

***

### TABLA 10: CÁLCULATOR ROI INTERACTIVA

| Métrica                   | Input               | Fórmula                            | Output  |
| ------------------------- | ------------------- | ---------------------------------- | ------- |
| **Setup Cost**            | User enters         | Manual                             | $X      |
| **Monthly Inference**     | user requests/month | X × $0.003                         | $Y      |
| **Monthly Fine-tuning**   | if yes              | Manual                             | $Z      |
| **Time Savings**          | Hours saved/month   | X × hourly rate                    | $W      |
| **Total Monthly Cost**    |                     | Y + Z                              | \$$$    |
| **Total Monthly Benefit** |                     | W                                  | \$$$    |
| **Payback Period**        |                     | Setup / (W - (Y+Z))                | M meses |
| **12-Month ROI**          |                     | ((W - (Y+Z)) × 12 - Setup) / Setup | X%      |

Ejemplo calculado:

```
Setup cost: $5,000
Monthly inference: 1M queries × $0.003 = $3,000
Monthly fine-tuning: $200
Time savings: 200 horas × $50/hr = $10,000
Net benefit/month: $10,000 - $3,200 = $6,800
Payback period: $5,000 / $6,800 = 0.7 meses ✓
12-Month ROI: ($6,800 × 12 - $5,000) / $5,000 = 1,630% ✓✓✓
```

***

### TABLA 11: GLOSARIO INTERACTIVA (LINKED)

Cada término en \[178] GLOSARIO tiene:

| Campo                    | Valor                          |
| ------------------------ | ------------------------------ |
| **Término**              | Nombre del concepto            |
| **Definición**           | Explicación clara              |
| **Contexto MiPyME**      | Aplicación real                |
| **Guías relacionadas**   | Links a secciones              |
| **Nivel complejidad**    | Beginner/Intermediate/Advanced |
| **Última actualización** | Fecha                          |
| **Links**                | A otras fichas relacionadas    |

***

## CÓMO USAR LA MACROTABLA

A continuación se presentan los flujos principales como steppers para guiar al usuario paso a paso.

{% stepper %}
{% step %}
### Flujo: "¿Por dónde empiezo?"

1. Abre **Tabla 1: Decisiones Iniciales**
2. Responde 5 preguntas clave
3. Sistema te recomienda:
   * Cuál guía leer
   * Qué tablas revisar
   * Tiempo estimado
   * Stack recomendado
{% endstep %}

{% step %}
### Flujo: "Tengo un problema"

1. Abre **Tabla 6: Problemas y Soluciones**
2. Busca tu problema
3. Lee solución
4. Abre la guía referenciada para más detalles
5. Revisa el tiempo estimado de fix en la tabla
{% endstep %}

{% step %}
### Flujo: "Quiero entender un concepto"

1. Abre **Tabla 11: Glosario Interactiva**
2. Busca término
3. Lee definición + contexto
4. Sigue links a guías relacionadas
5. (Opcional) Guardar en Notion/Obsidian
{% endstep %}

{% step %}
### Flujo: "Estoy en semana X de roadmap"

1. Abre **Tabla 4: Roadmap 12 Semanas**
2. Encuentra tu semana
3. Lee objetivo + horas
4. Abre guías linkedadas
5. Ejecuta las tareas planificadas
{% endstep %}

{% step %}
### Flujo: "Necesito calcular ROI"

1. Abre **Tabla 10: Calculator ROI**
2. Ingresa tus números:
   * Setup cost
   * Monthly request volume
   * Hourly rate ahorrado
3. Sistema calcula:
   * Payback period
   * 12-month ROI
   * Break-even point
{% endstep %}
{% endstepper %}

***

## SETUP AIRTABLE DESDE CERO

{% stepper %}
{% step %}
### Crear Base

1. Ve a airtable.com
2. Click "Create new base"
3. Nombre: "Llama MiPyME Hub"
4. Descripción: "Navegación + decisiones para 750 pgs IA"
{% endstep %}

{% step %}
### Crear Tablas

Copiar cada tabla de este documento a Airtable:

* TABLE > Create table > Name: "Decisiones Iniciales"
  * FIELD 1: Pregunta (Text)
  * FIELD 2: Respuesta Corta (Text)
  * FIELD 3: Documentos Relacionados (Linked Records)
  * FIELD 4: Tiempo Lectura (Number)
  * FIELD 5: Prioridad (Single Select)

\[Repeat para cada tabla listada en este documento]
{% endstep %}

{% step %}
### Rellenar Registros

Copiar datos de cada tabla aquí arriba a Airtable (puedes usar CSV o scripts de importación).
{% endstep %}

{% step %}
### Crear Vistas

Crear al menos estas vistas:

* Grid view (tabla)
* Gallery view (cards)
* Calendar (roadmap)
* Form (ROI calculator)
* Kanban (por status)
{% endstep %}

{% step %}
### Compartir

Share button → Generate link\
Compartir con team/estudiantes
{% endstep %}
{% endstepper %}

***

## PLANTILLA EXPORTABLE

CSV ejemplo para importar decisiones:

```
decision_key,question,short_answer,guide_ids,time_minutes,priority
dec001,"¿Local o cloud?","Depende tus reqs",172;173;174;175,5,HIGH
dec002,"¿Qué complejidad?","De principiante a avanzado",167;172;177,10,HIGH
dec003,"¿Necesito compliance?","LFPDPPP es crítico",175;178,15,HIGH
...
```

(Disponible para descarga como CSV + Excel)

***

## ACTUALIZACIÓN MENSUAL

Esta macrotabla será actualizada:

* Cada vez que sale Llama nueva versión
* Con feedback de usuarios
* Nuevos conceptos agregados al glosario
* New tools/frameworks

<details>

<summary>Changelog</summary>

* Nov 24, 2025: v1.0 (Initial release)
* Dic 2025: v1.1 (Llama 4 launch)
* Ene 2026: v2.0 (Esperado)

</details>

Última actualización: Noviembre 24, 2025\
Version: 1.0\
Total campos: 100+\
Total registros: 200+\
Status: Pronto en Airtable público

***

## SIGUIENTES PASOS

1. Crear base Airtable
2. Copiar todas las tablas
3. Llenar registros
4. Crear vistas inteligentes
5. Compartir link público
6. Publicar en Obsidian + GitBook

¿LISTO? 🚀

***

Si quieres, puedo:

* Generar los CSVs listos para importar para cada tabla.
* Preparar un script de importación (Airtable API) con los campos mapeados.
* Exportar versiones en Notion/Obsidian markdown. ¿Cuál prefieres?
