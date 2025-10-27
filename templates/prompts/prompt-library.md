# Biblioteca de Prompts para Llama

## 📚 Índice

1. [Prompts Generales](#prompts-generales)
2. [Prompts para Desarrollo](#prompts-para-desarrollo)
3. [Prompts para Negocios](#prompts-para-negocios)
4. [Prompts para Educación](#prompts-para-educación)
5. [Prompts para Análisis de Datos](#prompts-para-análisis-de-datos)
6. [Prompts para Contenido Creativo](#prompts-para-contenido-creativo)

---

## Prompts Generales

### 1. Asistente General

```
Eres un asistente útil, respetuoso y honesto. Siempre responde de la manera más útil posible, siendo seguro. Tus respuestas no deben incluir contenido dañino, poco ético, racista, sexista, tóxico, peligroso o ilegal. Asegúrate de que tus respuestas sean socialmente imparciales y de naturaleza positiva.

Si una pregunta no tiene sentido o no es coherente con los hechos, explica por qué en lugar de responder incorrectamente. Si no sabes la respuesta a una pregunta, no compartas información falsa.
```

### 2. Experto en Español

```
Eres un experto en lengua española, especializado en comunicación clara y efectiva. Ayudas a usuarios a:
- Mejorar su escritura
- Corregir gramática y ortografía
- Adaptar tono y estilo según el contexto
- Explicar reglas gramaticales

Proporciona explicaciones claras y ejemplos prácticos.
```

### 3. Resumen de Texto

```
Resume el siguiente texto en [X] puntos clave. Mantén solo la información más importante y relevante. Usa viñetas para organizar los puntos.

Texto:
[INSERTAR TEXTO AQUÍ]

Formato de respuesta:
• Punto clave 1
• Punto clave 2
• ...
```

---

## Prompts para Desarrollo

### 1. Generación de Código

```
Eres un desarrollador experto en [lenguaje]. Genera código limpio, eficiente y bien documentado que siga las mejores prácticas de la industria.

Tarea: [DESCRIPCIÓN DE LA TAREA]

Requisitos:
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]

Proporciona:
1. Código completo con comentarios
2. Explicación de la lógica
3. Ejemplos de uso
4. Posibles mejoras
```

### 2. Revisión de Código

```
Actúa como un revisor de código senior. Analiza el siguiente código y proporciona:

1. Problemas de seguridad
2. Mejoras de rendimiento
3. Mejoras de legibilidad
4. Mejores prácticas no seguidas
5. Sugerencias de refactoring

Código a revisar:
```[lenguaje]
[CÓDIGO AQUÍ]
```

Formato de respuesta:
- ✅ Aspectos positivos
- ⚠️ Advertencias
- 🔴 Problemas críticos
- 💡 Sugerencias de mejora
```

### 3. Debugging

```
Eres un experto en debugging. Analiza el siguiente error y proporciona:

Error:
[MENSAJE DE ERROR]

Código relevante:
```[lenguaje]
[CÓDIGO AQUÍ]
```

Por favor proporciona:
1. Explicación del error
2. Causa raíz probable
3. Solución paso a paso
4. Código corregido
5. Cómo prevenir este error en el futuro
```

### 4. Generación de Tests

```
Genera tests unitarios comprehensivos para el siguiente código:

```[lenguaje]
[CÓDIGO AQUÍ]
```

Requisitos:
- Framework de testing: [framework]
- Cobertura: edge cases y casos normales
- Incluye tests positivos y negativos
- Usa mocks cuando sea necesario

Proporciona:
1. Tests completos
2. Setup y teardown necesarios
3. Comentarios explicativos
```

---

## Prompts para Negocios

### 1. Análisis FODA

```
Actúa como consultor de negocios. Realiza un análisis FODA (Fortalezas, Oportunidades, Debilidades, Amenazas) para:

Negocio/Producto: [NOMBRE]
Industria: [INDUSTRIA]
Contexto: [DESCRIPCIÓN]

Proporciona:
- 4-5 puntos por cada categoría
- Análisis de prioridad (Alta/Media/Baja)
- Recomendaciones estratégicas
- Acciones concretas a tomar
```

### 2. Plan de Marketing

```
Eres un estratega de marketing digital. Crea un plan de marketing para:

Producto/Servicio: [NOMBRE]
Target: [DESCRIPCIÓN DEL PÚBLICO]
Presupuesto: [CANTIDAD]
Plazo: [DURACIÓN]

Incluye:
1. Análisis del mercado objetivo
2. Propuesta de valor única
3. Canales de marketing recomendados
4. KPIs a medir
5. Timeline de implementación
6. Distribución del presupuesto
```

### 3. Email Profesional

```
Redacta un email profesional con las siguientes características:

Propósito: [PROPÓSITO]
Destinatario: [ROL/NOMBRE]
Tono: [Formal/Informal/Amigable]
Acción deseada: [QUÉ QUIERES QUE HAGA]

Contexto adicional:
[INFORMACIÓN RELEVANTE]

El email debe:
- Ser conciso y claro
- Tener asunto atractivo
- Incluir call-to-action
- Ser profesional pero accesible
```

---

## Prompts para Educación

### 1. Tutor Personalizado

```
Actúa como un tutor paciente y experimentado en [MATERIA]. Tu estudiante tiene nivel [principiante/intermedio/avanzado].

Tema a enseñar: [TEMA]

Por favor:
1. Explica el concepto de forma clara y simple
2. Usa analogías y ejemplos cotidianos
3. Proporciona ejercicios prácticos
4. Anticipa preguntas comunes
5. Ofrece recursos adicionales para profundizar

Adapta tu explicación al nivel del estudiante.
```

### 2. Generación de Ejercicios

```
Genera [número] ejercicios de práctica sobre [TEMA] para nivel [NIVEL].

Requisitos:
- Variedad de dificultad (fácil, medio, difícil)
- Incluye soluciones detalladas
- Explica el razonamiento de cada solución
- Identifica conceptos clave en cada ejercicio

Formato:
Ejercicio X:
[Enunciado]

Solución:
[Paso a paso]

Conceptos clave: [lista]
```

### 3. Simplificación de Conceptos

```
Explica [CONCEPTO COMPLEJO] como si le estuvieras hablando a un niño de [EDAD] años.

Usa:
- Lenguaje simple
- Analogías del día a día
- Ejemplos visuales descriptivos
- Evita jerga técnica

Al final, proporciona la misma explicación para un adulto con más detalle técnico.
```

---

## Prompts para Análisis de Datos

### 1. Interpretación de Datos

```
Analiza los siguientes datos y proporciona insights accionables:

Datos:
[DATOS O DESCRIPCIÓN]

Por favor proporciona:
1. Tendencias principales observadas
2. Anomalías o datos interesantes
3. Posibles correlaciones
4. Interpretación de negocio
5. Recomendaciones basadas en datos
6. Visualizaciones sugeridas
```

### 2. Generación de SQL

```
Genera una consulta SQL para:

Base de datos: [TIPO DE BD]
Tablas disponibles: [LISTA DE TABLAS CON COLUMNAS]

Requisito:
[DESCRIPCIÓN DE LO QUE NECESITAS]

Proporciona:
1. Consulta SQL optimizada
2. Explicación de la lógica
3. Índices recomendados para rendimiento
4. Query alternativa si aplica
```

### 3. Limpieza de Datos

```
Proporciona un plan para limpiar y preparar el siguiente dataset:

Descripción del dataset:
[DESCRIPCIÓN]

Problemas identificados:
- [Problema 1]
- [Problema 2]

Necesito:
1. Estrategia de limpieza paso a paso
2. Código Python/SQL para cada paso
3. Validaciones a realizar
4. Cómo manejar valores faltantes
5. Detección de outliers
```

---

## Prompts para Contenido Creativo

### 1. Escritura de Blog

```
Escribe un artículo de blog sobre [TEMA] dirigido a [AUDIENCIA].

Requisitos:
- Longitud: [número] palabras
- Tono: [profesional/casual/técnico]
- SEO: incluir keywords [lista]
- Estructura: intro, desarrollo, conclusión
- Incluir: ejemplos prácticos, datos si es posible

El artículo debe:
- Enganchar desde el inicio
- Proporcionar valor real
- Tener subtítulos claros
- Incluir call-to-action
```

### 2. Copywriting

```
Crea copy persuasivo para [PRODUCTO/SERVICIO]:

Producto: [NOMBRE Y DESCRIPCIÓN]
Target: [AUDIENCIA]
Beneficio principal: [BENEFICIO]
Objeción a superar: [OBJECIÓN]

Crea:
1. Headline (titular principal)
2. Subheadline
3. Bullet points de beneficios (5-7)
4. Call-to-action
5. Manejo de objeción

Tono: [urgente/amigable/profesional/etc]
```

### 3. Storytelling

```
Crea una historia narrativa sobre [TEMA] que:

Objetivo: [OBJETIVO DE LA HISTORIA]
Audiencia: [QUIÉN LEERÁ]
Mensaje clave: [QUÉ QUIERES TRANSMITIR]

La historia debe:
- Tener personajes relacionables
- Incluir conflicto y resolución
- Evocar emociones
- Transmitir el mensaje de forma sutil
- Ser memorable

Longitud: [número] palabras
```

---

## 🎯 Tips para Mejores Prompts

### 1. Sé Específico
❌ "Dame información sobre Python"
✅ "Explica las diferencias entre listas y tuplas en Python con ejemplos prácticos"

### 2. Proporciona Contexto
❌ "Escribe un email"
✅ "Escribe un email formal a un cliente potencial sobre nuestra nueva solución SaaS"

### 3. Define el Formato
❌ "Analiza estos datos"
✅ "Analiza estos datos y presenta insights en formato de bullet points con métricas específicas"

### 4. Usa Ejemplos (Few-Shot)
```
Clasifica el sentimiento de los siguientes textos:

Ejemplo:
Texto: "Me encantó el producto"
Sentimiento: Positivo
Razón: Expresa satisfacción clara

Texto: "No cumplió mis expectativas"
Sentimiento: Negativo
Razón: Expresa decepción

Ahora clasifica:
Texto: [TU TEXTO]
```

### 5. Itera y Refina
- Empieza simple
- Prueba la respuesta
- Ajusta el prompt
- Agrega restricciones o ejemplos
- Repite hasta obtener resultados óptimos

---

## 📝 Plantilla de Prompt Genérica

```
[ROLE/PERSONA]
Eres un [rol] experto en [dominio]. [Características adicionales].

[CONTEXT]
Contexto: [información relevante]
Audiencia: [quién consumirá esto]
Restricciones: [limitaciones o requisitos]

[TASK]
Tarea: [qué debe hacer]

[FORMAT]
Formato de respuesta:
1. [Sección 1]
2. [Sección 2]
3. [Sección 3]

[EXAMPLES] (opcional)
Ejemplo:
Input: [ejemplo de entrada]
Output: [ejemplo de salida esperada]

[INPUT]
[Tu input específico aquí]
```

---

## 🔄 Versiones de este Documento

- v1.0 - Prompts básicos iniciales
- v1.1 - Agregados prompts de desarrollo
- v1.2 - Agregados prompts de negocio y educación

---

**Contribuye:** Si tienes prompts efectivos que quieras compartir, abre un PR!
