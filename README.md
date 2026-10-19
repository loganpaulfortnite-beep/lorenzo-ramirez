# Lorenzo Ramírez — Motor visual de videoensayos

Proyecto para transformar fragmentos de **Despegamos** en vídeos documentales faceless con apoyo visual preciso y edición de calidad.

## Cómo utilizarlo en Codex

Abre este repositorio en Codex y solicita:

> Utiliza $despegamos-visual-premium para procesar este episodio de Despegamos: [URL]. Crea un vídeo documental de 10 minutos, 1080p. Usa las voces originales, vídeos reales vinculados a cada intervención, y motion graphics solo cuando expliquen un mecanismo que el metraje no pueda mostrar. No repitas recursos. Revisa y valida el resultado.

La skill está en `.agents/skills/despegamos-visual-premium/SKILL.md`. Las reglas generales están en `AGENTS.md`.

## Motor recomendado

- **Remotion + React/SVG**: composiciones de vídeo y animaciones editoriales.
- **FFmpeg**: cortes, audio, exportación, control de calidad.
- **faster-whisper**: transcripción con tiempos por palabra.
- **MapLibre**: mapas cuando se mencionan localizaciones concretas; comprobar licencia de los mapas base.
- **Manim CE**: opcional, únicamente para visualizaciones matemáticas que lo justifiquen.
- **Higgsfield**: opcional; solo para un plano de apoyo que no se encuentre de forma legítima.

Instalación de las skills oficiales de Remotion dentro del proyecto, cuando Codex las necesite:

```bash
npx skills add remotion-dev/skills
```

La instalación exige Node.js y acceso a Internet. La skill de este repositorio **no ejecuta por sí sola** un episodio entero: define las decisiones editoriales y validadores, y Codex organiza la búsqueda, animación y render.

## Validación

```bash
python3 .agents/skills/despegamos-visual-premium/scripts/validate_storyboard.py path/to/storyboard.json
python3 -m unittest discover -s .agents/skills/despegamos-visual-premium/scripts -p 'test_*.py'
```

**No se publica** un vídeo cuando las comprobaciones de sincronía, procedencia de clips, licencias o correspondencia semántica no estén resueltas.
