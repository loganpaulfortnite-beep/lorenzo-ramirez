# Fuentes de recursos y verificación

## Orden de búsqueda

1. **Fuente primaria nombrada por el locutor**: vídeos oficiales de ASML, Banco Central Europeo, Comisión Europea, Parlamento Europeo, Ministerio, TSMC; oficinas de prensa, canales oficiales, portales institucionales y vídeos originales del acto concreto. No asumir permiso de reutilización por estar publicado.
2. **Archivos y medios con licencia explícita**: Wikimedia Commons con licencia por activo, plataformas de vídeo con licencia realmente válida para ese archivo concreto. Mixkit tiene Free y Restricted — verificar qué régimen aplica; Pexels o Pixabay con licencia vigente y condiciones del activo.
3. **Vídeo documental ilustrativo**: filmación de un procedimiento real que coincida, aunque no sea la persona exacta. Marcarlo como ilustrativo cuando pueda confundirse con la noticia.
4. **Foto histórica**: solo cuando aporta evidencia imposible de sustituir por vídeo.
5. **Motion graphics**: exclusivamente para mostrar relaciones, causalidad, escala, rutas, interfaces verificadas o estadísticas sustentadas.

## Ledger obligatorio por recurso

Guardar asset_id, URL exacta, sitio, fuente primaria, titular/descripción, licencia identificada, URL de licencia, autor, fecha/ubicación, resolución, fps, duración, hash SHA-256 del archivo, tiempo de uso, cita narrada y motivo de selección.

Una URL a una página de la entidad NO implica permiso. Un clip de agencia de noticias suele requerir licencia específica. Un vídeo de YouTube no pasa a ser libre por poder descargarse. No extraer 10 minutos de otra obra sin revisar derechos ni dar por hecho que basta una atribución.

## Correspondencia semántica

Separar **identidad del sujeto** de **equivalencia temática**.

- Si se menciona la fábrica de ASML en Veldhoven, una fábrica cualquiera no vale como vídeo documental de ASML.
- Si se menciona la firma de un acuerdo, la fachada de una institución puede ser contextual, pero no representar la firma.
- Si se menciona un supuesto espionaje, imágenes de hackers encapuchados no prueban la historia; usar prueba publicada o representación expresamente conceptual.
- No usar tres clips diferentes del mismo archivo fuente considerándolos "únicos". Guardar `source_fingerprint` además de hash.
- No confundir el edificio de Google de Toronto con una sede de España; si está identificado, puede representar Google como empresa, pero el rótulo no debe falsear la localización.
- En citas controvertidas, priorizar evidencia y contexto original; no sugerir culpabilidad mediante montaje engañoso.

## Mapas

MapLibre GL JS funciona con diferentes proveedores de teselas: verificar licencia, términos y atribución del basemap utilizado. Evitar Google Earth Studio en producciones comerciales por defecto: su documentación restringe usos comerciales y exige atribución visual. El motor de mapas no garantiza licencia de los datos cartográficos.

## Control de derechos antes de publicar

Conservar ledger y capturas de licencia o términos aplicables, usar vídeo propio/permiso explícito cuando la licencia no está clara, y eliminar/reemplazar los clips sin base legal verificable. En España, revisar además el régimen de cita y límites de uso; no existe una excepción automática por llamar al vídeo "educativo".

Links útiles:
- https://commons.wikimedia.org/wiki/Commons:Licensing
- https://mixkit.co/license/
- https://www.remotion.dev/docs/license
- https://www.google.com/intl/es/earth/studio/faq/
