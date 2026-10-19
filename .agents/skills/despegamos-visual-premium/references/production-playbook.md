# Plan de ejecución de Codex: un episodio

## Antes de codificar

- Consultar la skill y la documentación vigente de Remotion.
- Generar transcripción de palabras (faster-whisper --word_timestamps) y guardar original y hash.
- Encontrar el bloque de 10 min que contenga un argumento claro, identificando cortes y evitando alterar significado.
- Buscar vídeo, archivo y noticias utilizando consultas concretas (persona, organismo, ciudad, acto, fecha, idioma, modelo de máquina).
- **No crear 30 diagramas por adelantado:** marcar primero las explicaciones que requieren visualizar relaciones.

## Organización de carpetas recomendada

- episodes/2026-10-15/source/audio_original.mp3
- episodes/2026-10-15/analysis/transcript_words.json
- episodes/2026-10-15/analysis/storyboard.json
- episodes/2026-10-15/analysis/rights_ledger.csv
- episodes/2026-10-15/media/video/...
- episodes/2026-10-15/media/archive/...
- episodes/2026-10-15/graphics/...
- episodes/2026-10-15/previews/...
- episodes/2026-10-15/output/final_1080p.mp4

Evitar dependencias múltiples para la misma tarea. Node.js/Remotion/FFmpeg y Python con faster-whisper son suficientes para el 90 % de los casos. No hace falta DaVinci ni After Effects para ejecutar el motor inicial.

## Implementar composiciones

- Una composición React/Remotion por microhistoria (no un componente gigante de 10 minutos).
- Control del fotograma con useCurrentFrame/useVideoConfig; keyframes por timestamps reales.
- Cámara sobre imágenes reales: movimientos de enfoque discretos; NO confundir parallax con secuencia documental.
- Gráficos: geometría de objetos y conexiones específica, pantalla construida paso a paso, fuente verificable.
- Mapas: coordenadas verificadas y diseños contrastados; no animaciones irreales de una ciudad equivocada.
- Datos: graficar la serie verdadera, no datos inventados para rellenar.
- Conservar los archivos originales para atribución y no comprimir repetidamente.

## QA en tres barreras

1. **Preproducción**: revisar 30 intervenciones de ejemplo. Si más del 10 % no tienen una correspondencia específica, no pasar al render.
2. **Preview**: render de 30 segundos con ejemplos de cada lenguaje visual (metraje auténtico, mapa, documento y gráfico técnico). Revisar composición y precisión contra el audio.
3. **Exportación**: validar storyboard + derechos + 1080p + fps + duración + colas de audio + duplicados + 5 fotogramas distribuidos por cada minuto + inspección total a velocidad real.

No establecer porcentajes obligatorios de gráficos ni tiempos fijos para cada recurso. La longitud de cada toma la dicta la explicación.

## Extra: fotografía de archivo vs vídeo

Una foto estática puede ser la evidencia correcta si es un hecho sin vídeo, pero no es un sustituto para un archivo audiovisual que sí existe.

Evitar B-roll contextual equívoco: un documento oficial puede ser útil como fuente sin que se muestre como evidencia de una conspiración o delito. Separar con claridad las declaraciones del locutor y las conclusiones sustentadas.

## Dependencias útiles, solo bajo demanda

- Node.js + Remotion y skill oficial: npx skills add remotion-dev/skills
- Remotion Maps / MapLibre para geografía.
- Manim CE si el episodio incluye geometría matemática avanzada.
- Adobe After Effects y GEOlayers solo para un operador humano cuando el resultado no sea alcanzable de forma eficiente con código.

## Prompts operativos

- "Primero dame una tabla de 20 shots con audio exacto, URL real del metraje y motivo editorial; rechaza los recursos genéricos."
- "Para los conceptos que requieren gráfico, crea una pregunta visual y una progresión física verificable, no cajas decorativas."
- "Antes del render, ejecuta validate_storyboard.py; devuelve bloqueantes concretos. No reportes validado si faltan archivos o permisos."
- "Usa las reglas de la skill y genera un preview de 30 segundos con ASML/EUV, cartera EUDI y euro digital como sistemas distintos."
