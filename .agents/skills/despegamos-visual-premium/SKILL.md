---
name: despegamos-visual-premium
description: Producción y revisión de videoensayos faceless premium a partir de podcasts de Despegamos o Lorenzo Ramírez. Busca B-roll y archivo documental específico por frase y crea motion graphics editoriales profesionales solo cuando ayuden a explicar conceptos complejos. Sin vídeos repetidos, gráficos infantiles, activos inventados ni desincronización. Utilízala cuando el usuario pida crear o mejorar sus vídeos documentales.
---

# Despegamos Visual Premium

No basta con renderizar 10 minutos. El producto es una interpretación audiovisual rigurosa de la conversación, equivalente en intención editorial a un documental de investigación.

## Flujo obligatorio

1. **Ingesta.** Obtener audio y transcripción con timings por palabra; identificar idioma, ponentes, huecos, referencias y entidades. Conservar fuente y duración. Descargar material de YouTube solo cuando se tenga derecho a usarlo; preferir RSS/feeds y fuentes autorizadas.
2. **Seleccionar un relato coherente.** Elegir una sección que funcione por sí sola. Reordenar o cortar solo cuando se mantenga el sentido; no unir frases alejadas fingiendo una declaración continua. Un teaser puede ser reordenado si se identifica claramente.
3. **Storyboard semántico.** Por cada intervención anotar timecodes exactos, palabras relevantes, entidad/lugar/objeto/proceso, lo que debe verse y por qué. Revisar el ledger antes de descargar. No inferir el tema visual solo de una palabra clave.
4. **Decisión de recurso, siempre por este orden:**
   - A. Vídeo real del objeto, hecho, persona o lugar exactos.
   - B. Vídeo de un proceso equivalente pero reconocido explícitamente como ilustrativo, nunca como una escena del hecho.
   - C. Documento, captura o archivo verificado, animado con discreción para dirigir la atención a un dato.
   - D. Motion graphic original **solo si** explica causalidad, secuencia, flujo, escala, ubicación, comparación o abstracción que no se entiende con A–C.
   - E. Un plano adicional generado con IA solo si el resto no funciona y no se representa falsamente como archivo.
5. **Buscar y verificar.** Fuentes primarias y oficiales para empresas, países, edificios, responsables políticos y mecanismos. Buscar primero nombres exactos, variantes e idioma nativo. Revisar derechos, fecha, localización y elementos visuales reales. Leer `references/sourcing.md`.
6. **Dirección de arte.** Para todo recurso D, escoger la mejor familia: recorte técnico en capas, mapa geográfico, cámara sobre documento, gráfico de datos con fuente, animación de proceso, compositing de interfaz real. Leer `references/motion-language.md`. No generar iconos redondos, tarjetas vistosas, fondos neon, pantallas de "datos" ficticios ni infografías terminadas de golpe.
7. **Sincronía.** Cada elemento aparece o cambia al pronunciarse su concepto; usar timestamps por palabra. Las animaciones tienen guion interno, no solo inicio y fin. No comprimir/acelerar la locución para acomodar el gráfico.
8. **Realización.** Preferir Remotion/React/SVG + FFmpeg; usar la skill oficial `remotion-dev/skills` para APIs modernas y Remotion Maps si aplica. Manim solamente en visualizaciones matemáticas complejas. No obligar a Higgsfield a producir 60 bloques abstractos si con clips reales se cuenta mejor la historia.
9. **QA en dos pases.** A) semántico: ver y escuchar juntos cada secuencia; marcar desajustes y eliminar recursos de relleno. B) técnico: continuidad, niveles de audio, derechos, legibilidad, música, artefactos, fuentes, duración, resolución. Validar el JSON de storyboard con `scripts/validate_storyboard.py`. Renderizar 20–40 s representativos antes de exportar diez minutos.
10. **Entrega.** Un MP4 comprobado, storyboard JSON, ledger de licencias y fuentes, lista de gráficos y pendientes verificados. Si algo no está validado, indicarlo; nunca confundir "render terminado" con "nivel profesional".

## Prohibiciones de calidad

- Una imagen estática como sustituto sistemático de vídeo; vídeo genérico de ordenador mientras se cita ASML; archivos de hackers mientras se habla de Palantir sin relación concreta.
- Recursos repetidos o plantillas gráficas solo recoloreadas. Un gráfico de nodos sin nombres/causalidad real no explica nada.
- Texto de gran tamaño sobre cada escena, stock surrealista, animación de parvulario, proporciones inventadas y cifras no contrastadas.
- "Demostraciones" inventadas de un programa gubernamental, una tecnología operativa o una persona en un acto real.
- Establecer una cuota fija de gráficos. El metraje real ocupa todo el tiempo que pueda sostenerse sin perder comprensión.

## Selección de gráficos

Antes de aceptar un gráfico, responder: ¿qué relación nueva entenderá el espectador que no entiende viendo el metraje real? Si la respuesta es "ninguna", eliminarlo. El gráfico debe añadir información, no atmósfera.

## Contratos y referencias

- `references/motion-language.md` — gramática y ejemplos de dirección de arte.
- `references/sourcing.md` — procedimiento de metraje, archivo, derechos y verificación.
- `references/shot-contract.md` — JSON por shot, sincronía y QA.
- `scripts/validate_storyboard.py` — validador determinista. Pasar obligatoriamente antes de render final.
- `scripts/test_validate_storyboard.py` — pruebas negativas y positivas.
- Skill oficial de Remotion: https://github.com/remotion-dev/skills .

## Criterio de éxito

El resultado debe seguir pudiéndose entender visualmente sin subtítulos. Los gráficos deben parecer trabajo editorial específico y pensado, no un salvapantallas informativo. La primera persona que revise el proyecto debe poder identificar el archivo fuente y el motivo visual de cada shot.
