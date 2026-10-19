# Contrato del storyboard y validación

Un proyecto debe emitir un JSON que pase `scripts/validate_storyboard.py` antes de exportar.

Formato mínimo:

```json
{
  "duration": 12.0,
  "fps": 25,
  "width": 1920,
  "height": 1080,
  "shots": [
    {
      "id": "s001",
      "start": 0.0,
      "end": 5.0,
      "narration": "La empresa que construye las máquinas...",
      "semantic_target": "ASML, maquinaria de litografía EUV",
      "visual_type": "video",
      "asset_id": "asml_official_2026_001",
      "asset_path": "media/asml_euv_01.mp4",
      "source_fingerprint": "youtube-channel:asml:video-abc123",
      "source_url": "https://example.org/real-asset",
      "license": "rights-cleared",
      "license_url": "https://example.org/permission",
      "match_reason": "Vídeo genuino de maquinaria ASML, no imágenes de informática genérica",
      "verified": true
    },
    {
      "id": "s002",
      "start": 5.0,
      "end": 12.0,
      "narration": "La luz se proyecta sobre una oblea...",
      "semantic_target": "mecanismo de litografía explicado como modelo simplificado",
      "visual_type": "graphic",
      "graphic_id": "euv-process-cutaway-01",
      "graphic_question": "¿Cómo se transfiere el patrón a una oblea?",
      "graphic_storyboard": [
        "Aparece la fuente de EUV",
        "Trayectoria óptica con espejos reflectivos",
        "La imagen del patrón alcanza la oblea"
      ],
      "data_source": "https://example.org/technical-explanation",
      "why_graphic": "El mecanismo óptico interno no se comprende con el plano exterior",
      "match_reason": "Explicación técnica sincronizada a la narración",
      "verified": true
    }
  ]
}
```

Los dominios `example.org` son solo marcadores didácticos; en producción deben reemplazarse por fuentes auténticas.

Tipos: video, archive, graphic, map, chart, document. Para videos y archivo son obligatorios `asset_id, source_fingerprint, source_url, license, license_url, match_reason`. Para mapas/gráficos además se exige `data_source`. Para gráficos un `graphic_id` único, pregunta cognitiva y pasos reales de transformación.

**Evitar declarar `verified: true` hasta haber comprobado el vídeo, la relación semántica y la licencia.** No basta la coincidencia de términos.

La línea temporal debe ser continua, sin huecos ni solapamientos superiores a 80 ms. No repetir asset IDs, source fingerprints o graphic IDs dentro de un episodio.

Objetivo creativo: ningún gráfico aparece por cuota. Los gráficos deben responder una pregunta cognitiva comprobable y ser renderizables con geometría/capas y tiempo vinculados a la narración.
