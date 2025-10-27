# Assets - Recursos Visuales

Esta carpeta contiene todos los recursos visuales del proyecto.

## 📁 Estructura

```
assets/
├── images/           # Imágenes generales (logos, banners)
├── diagrams/         # Diagramas técnicos y de arquitectura
└── screenshots/      # Capturas de pantalla de demos
```

## 🖼️ Contenido

### Images
- Logo del proyecto
- Banner principal
- Iconos
- Ilustraciones

### Diagrams
- Diagramas de arquitectura
- Flujos de trabajo
- Diagramas de sistemas RAG
- Esquemas técnicos

### Screenshots
- Demos de aplicaciones
- Ejemplos de resultados
- Interfaces de usuario
- Tutoriales visuales

## 📝 Guía de Contribución

### Formato de Imágenes

- **Logos**: PNG con fondo transparente
- **Screenshots**: PNG o JPG (máx 2MB)
- **Diagramas**: SVG preferido, PNG como alternativa

### Nomenclatura

```
tipo-descripcion-version.extension

Ejemplos:
- logo-llama-main.png
- diagram-rag-architecture-v1.svg
- screenshot-chatbot-demo.png
```

### Optimización

Antes de agregar imágenes:
1. Optimiza el tamaño (usar herramientas como TinyPNG)
2. Verifica la calidad
3. Usa nombres descriptivos
4. Agrega alt text en markdown

### Uso en Markdown

```markdown
# Logo
![Llama Workshop](../assets/images/logo-llama-main.png)

# Diagrama con descripción
![Arquitectura RAG](../assets/diagrams/diagram-rag-architecture-v1.svg)
*Diagrama de arquitectura del sistema RAG*

# Screenshot con tamaño
<img src="../assets/screenshots/screenshot-chatbot-demo.png" alt="Demo Chatbot" width="600">
```

## 📄 Licencia

Las imágenes en este directorio están sujetas a las mismas licencias que el proyecto:
- Recursos creados por nosotros: CC BY 4.0
- Logos de terceros: Respetan sus licencias originales

## 🎨 Guía de Estilo Visual

### Colores Principales

```
Primario: #667eea (Púrpura)
Secundario: #764ba2 (Morado)
Acento: #48bb78 (Verde)
Texto: #2d3748 (Gris oscuro)
Fondo: #ffffff (Blanco)
```

### Tipografía

- **Headings**: System fonts (-apple-system, BlinkMacSystemFont, 'Segoe UI')
- **Body**: Roboto, Arial, sans-serif
- **Code**: 'Fira Code', 'Courier New', monospace

## 📚 Recursos Externos

Si necesitas crear recursos visuales:

- **Diagramas**: [Excalidraw](https://excalidraw.com/), [Draw.io](https://draw.io/)
- **Iconos**: [Heroicons](https://heroicons.com/), [Feather Icons](https://feathericons.com/)
- **Ilustraciones**: [unDraw](https://undraw.co/)
- **Optimización**: [TinyPNG](https://tinypng.com/), [Squoosh](https://squoosh.app/)

## ✅ Checklist para Nuevas Imágenes

- [ ] Imagen optimizada para web
- [ ] Nombre descriptivo y consistente
- [ ] Tamaño apropiado (< 2MB para screenshots)
- [ ] Formato correcto (SVG para diagramas, PNG/JPG para fotos)
- [ ] Alt text proporcionado en uso
- [ ] Licencia verificada (si es de terceros)
- [ ] Documentado en este README si es relevante

---

**Última actualización**: Octubre 2025
