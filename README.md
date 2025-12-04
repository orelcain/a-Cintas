# 📋 Sistema de Documentación Técnica - Cintas Transportadoras

Sistema web profesional para crear informes técnicos de cintas transportadoras con capacidad de documentación fotográfica, anotaciones visuales y exportación a múltiples formatos.

![Estado](https://img.shields.io/badge/Estado-Producción-success)
![Versión](https://img.shields.io/badge/Versión-2.0-blue)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

## 🎯 Características Principales

### 📸 Gestión de Imágenes
- **Carga masiva de fotos** por sección (banda y motor)
- **Almacenamiento en IndexedDB** (sin límite de tamaño)
- **Rotación y zoom** de imágenes
- **Descripciones personalizadas** para cada foto
- **Drag & drop** para reordenar imágenes

### ✏️ Anotaciones en Imágenes
- **5 herramientas de dibujo:**
  - ➤ Flechas con punta automática
  - ⭕ Círculos
  - ▭ Rectángulos
  - ✏️ Dibujo libre
  - T Texto
- **Selector de color** personalizado
- **Deshacer última anotación** (↶)
- **Borrar todas las anotaciones**
- **Canvas overlay** (no modifica imagen original)
- Las anotaciones se **guardan y exportan en PDF**

### 📊 Resumen Ejecutivo
- **Estadísticas automáticas:**
  - Total de cintas
  - Cintas con imágenes
  - Total de imágenes
  - Promedio de imágenes por cinta
- **Gráficos de distribución** por área con colores
- **Estado general** con código de colores

### 📄 Exportación PDF Profesional

#### 3 Plantillas Disponibles:
1. **PDF Ejecutivo** (📊)
   - Solo resumen ejecutivo
   - Estadísticas y gráficos
   - Información general

2. **PDF Técnico** (🔧)
   - Resumen ejecutivo
   - Todas las especificaciones técnicas
   - Sin imágenes (más liviano)

3. **PDF Completo** (📋)
   - Resumen ejecutivo
   - Especificaciones técnicas
   - Todas las imágenes con anotaciones
   - Descripciones de fotos

#### Configuración de Calidad:
- **Baja** (2-4 MB): Escala 2x, JPEG 70%
- **Media** (4-8 MB): Escala 3x, JPEG 85%
- **Alta** (8-15 MB): Escala 4x, JPEG 95%
- **Ultra** (15-30 MB): Escala 6x, JPEG 98%

#### Tamaños de Imagen:
- Pequeña (60mm)
- Mediana (85mm)
- Grande (110mm)
- Muy Grande (140mm)

### 📑 Tablas Dinámicas
- **Añadir/eliminar filas** con botones + y ×
- **Añadir/eliminar columnas** para comparativas
- **Múltiples tablas** por cinta
- **Campos editables** con autoexpansión
- **Copiar datos de motor** entre cintas

### 🎨 Personalización
- **Colores personalizables:**
  - Color principal (secciones)
  - Color de áreas
  - Color de encabezado
- **Logo de empresa** (guardado en IndexedDB)
- **Información de empresa** (nombre, planta, contacto, email)

### 📝 Metadatos de Inspección
- Fecha de inspección
- Técnico responsable
- Ubicación de planta
- Estado general (Operativo/Mantenimiento/Detenido/Crítico)
- Observaciones generales

### 💾 Almacenamiento y Respaldo
- **Autoguardado** cada segundo
- **IndexedDB** para imágenes y logo (sin límite)
- **localStorage** para datos de texto (~5-10 MB)
- **Exportar/Importar** datos completos con imágenes (JSON)
- **Exportar a Excel** con todas las especificaciones

## 🚀 Uso

### Instalación
No requiere instalación. Es una aplicación web de archivo único:

```bash
# Clonar el repositorio
git clone https://github.com/orelcain/a-Cintas.git

# Abrir el archivo HTML en navegador
# Recomendado: Chrome, Edge o Firefox
start cintas-planta-mejorado.html
```

### Primeros Pasos

1. **Configurar Encabezado**
   - Subir logo de empresa
   - Llenar información de empresa

2. **Agregar Metadatos**
   - Fecha de inspección
   - Técnico responsable
   - Ubicación y estado

3. **Crear Cintas**
   - Botón "➕ Agregar Nueva Cinta"
   - Definir área (ej: ÁREA FILETE)
   - Nombrar cinta

4. **Llenar Especificaciones**
   - Editar tablas de banda y motor
   - Agregar/eliminar filas según necesidad
   - Agregar columnas para comparativas

5. **Subir Fotos**
   - Botón "📷 Agregar Fotos"
   - Carga masiva disponible
   - Añadir descripciones

6. **Anotar Imágenes**
   - Pasar mouse sobre imagen
   - Seleccionar herramienta
   - Dibujar sobre la imagen
   - Cambiar color si necesario
   - Usar "↶" para deshacer

7. **Exportar**
   - Seleccionar plantilla PDF
   - Configurar calidad
   - Exportar PDF

## 🛠️ Tecnologías

- **HTML5** - Estructura
- **CSS3** - Estilos con gradientes y animaciones
- **JavaScript (Vanilla)** - Lógica de aplicación
- **IndexedDB API** - Almacenamiento de imágenes
- **localStorage API** - Almacenamiento de texto
- **Canvas API** - Anotaciones sobre imágenes
- **jsPDF** - Generación de PDFs
- **XLSX.js** - Exportación a Excel

## 📦 Dependencias CDN

```html
<!-- jsPDF 2.5.1 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<!-- jsPDF AutoTable 3.5.31 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.31/jspdf.plugin.autotable.min.js"></script>

<!-- html2canvas 1.4.1 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>

<!-- XLSX 0.18.5 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
```

## 🔧 Características Técnicas

### Almacenamiento
```javascript
// IndexedDB (sin límite)
- Imágenes en base64
- Logo de empresa
- Total: Ilimitado (dependiente del disco)

// localStorage (~5-10 MB)
- Metadatos de inspección
- Especificaciones técnicas
- Anotaciones (coordenadas)
- Configuración de colores
```

### Estructura de Datos
```javascript
{
  timestamp: "2025-12-03T...",
  annotations: {
    "image-id-1": [
      { type: "arrow", x1: 10, y1: 20, x2: 100, y2: 200, color: "#ff0000" },
      { type: "circle", x: 50, y: 50, radius: 30, color: "#00ff00" }
    ]
  },
  metadata: {
    fechaInspeccion: "2025-12-03",
    tecnicoResponsable: "Ing. Juan Pérez",
    ubicacionPlanta: "Planta Principal - Línea 1",
    estadoGeneral: "operativo",
    observacionesGenerales: "..."
  },
  header: {
    empresaNombre: "Mi Empresa S.A.",
    plantaNombre: "Planta Lima",
    contactoInfo: "+51 999 999 999",
    emailInfo: "contacto@empresa.com",
    hasLogo: true
  },
  cintas: [
    {
      id: 1,
      area: "ÁREA FILETE",
      titulo: "Cinta 1 - Transportadora Principal",
      tablas: [...],
      imagenes: { banda: [...], motor: [...] },
      descripciones: { "img-id": "Vista frontal motor" }
    }
  ]
}
```

## 📋 Casos de Uso

### Industria Alimentaria
- Documentación de cintas de fileteo
- Cintas de transporte de productos
- Líneas de procesamiento

### Manufactura
- Sistemas de transporte de materiales
- Líneas de ensamblaje
- Sistemas de distribución

### Mantenimiento Industrial
- Inspecciones programadas
- Levantamientos técnicos
- Reportes de estado

### Auditorías
- Documentación de equipos
- Reportes de compliance
- Verificaciones técnicas

## ⚠️ Requisitos del Navegador

### Recomendado
- ✅ Chrome 90+
- ✅ Edge 90+
- ✅ Firefox 85+

### Características Necesarias
- IndexedDB API
- Canvas API
- localStorage
- FileReader API
- Drag and Drop API

### Nota sobre Tracking Prevention
Si usas Edge/Safari con Tracking Prevention activado, puede haber problemas con IndexedDB. Solución:
1. Agregar el sitio a excepciones
2. Desactivar Tracking Prevention
3. Usar Chrome/Firefox

## 🔐 Seguridad y Privacidad

- ✅ **100% local** - No se envía nada a servidores
- ✅ **Sin internet requerido** (después de cargar CDNs)
- ✅ **Datos en tu navegador** - Total control
- ✅ **Sin cookies** ni tracking
- ✅ **Exportación completa** disponible siempre

## 📊 Rendimiento

### Tiempos Aproximados
- Carga inicial: < 1 segundo
- Autoguardado: < 100ms
- Exportación PDF Media (10 cintas, 50 fotos): 10-20 segundos
- Exportación PDF Ultra (10 cintas, 50 fotos): 30-60 segundos
- Importar datos completos: 2-5 segundos

### Capacidad
- Cintas: Ilimitadas (recomendado < 50)
- Imágenes por cinta: Ilimitadas (recomendado < 20)
- Tamaño de imagen: Recomendado < 5MB c/u
- Total proyecto: Limitado por espacio en disco

## 🐛 Solución de Problemas

### "Almacenamiento localStorage lleno"
**Causa:** Textos/observaciones muy largos  
**Solución:** 
1. Exportar datos completos (backup)
2. Acortar observaciones generales
3. Eliminar cintas antiguas

### Las imágenes no cargan
**Causa:** IndexedDB bloqueado por navegador  
**Solución:**
1. Verificar que IndexedDB está habilitado
2. Desactivar Tracking Prevention
3. Usar Chrome/Firefox

### PDF muy pesado
**Solución:**
1. Usar calidad "Baja" o "Media"
2. Reducir tamaño de imágenes
3. Usar plantilla "Técnico" (sin imágenes)

### Anotaciones no aparecen en PDF
**Causa:** Canvas no sincronizado  
**Solución:**
1. Guardar antes de exportar
2. Verificar que aparecen en pantalla
3. Recargar página y volver a intentar

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork del proyecto
2. Crear rama feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit cambios (`git commit -m 'Agregar NuevaCaracteristica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abrir Pull Request

## 📝 Changelog

### v2.0 (3 Diciembre 2025)
- ✅ Sistema completo de anotaciones en imágenes
- ✅ 5 herramientas de dibujo (flecha, círculo, rect, libre, texto)
- ✅ Función deshacer anotaciones
- ✅ Resumen ejecutivo con estadísticas
- ✅ 3 plantillas de PDF (Ejecutivo, Técnico, Completo)
- ✅ Exportación de anotaciones en PDF
- ✅ Optimización de almacenamiento (logo en IndexedDB)
- ✅ Fix: eventos de canvas para prevenir arrastre

### v1.5
- ✅ Descripciones de fotos
- ✅ Metadatos de inspección
- ✅ Encabezado personalizable con logo
- ✅ Personalización de colores
- ✅ Exportar/Importar datos completos

### v1.0
- ✅ Sistema base de cintas
- ✅ Tablas dinámicas
- ✅ Carga de imágenes
- ✅ Exportación PDF y Excel

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Orel Cain**
- GitHub: [@orelcain](https://github.com/orelcain)
- Proyecto: [a-Cintas](https://github.com/orelcain/a-Cintas)

## 🙏 Agradecimientos

- jsPDF por la librería de generación de PDFs
- SheetJS por la librería XLSX
- Comunidad open source

---

**¿Preguntas o sugerencias?** Abre un [issue](https://github.com/orelcain/a-Cintas/issues) en GitHub.

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub.
