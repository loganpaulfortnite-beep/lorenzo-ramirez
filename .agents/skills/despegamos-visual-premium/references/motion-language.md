# Lenguaje visual de documental premium

**Identidad:** realismo editorial, material histórico auténtico, cámara discreta, mapas cartográficos, recortes técnicos y movimiento motivado por la narrativa. No identidad de marca específica; inspirarse en principios de los videoensayos de Vox/Johnny Harris, del visual storytelling de 3Blue1Brown y del B-roll semántico de Adrián Díaz, sin clonar logotipos, animaciones ni activos.

## Banco de decisiones para motion graphics

| Explicación que necesita el espectador | Técnica correcta | Técnica a evitar |
| --- | --- | --- |
| ¿Dónde ocurre? | MapLibre/GeoJSON con frontera y posición reales; travelling entre localizaciones; marcador aparece cuando se cita | Banderas aleatorias, un mapa genérico mundial |
| ¿Cómo funciona una máquina? | Corte técnico con 3D/parallax, partes reales etiquetadas mínimamente, luz/trayectoria/flujo progresivos | Cinco círculos con iconos genéricos |
| ¿Cómo se relacionan 2 instituciones? | Logos originales verificados, recortes de edificios o documentación, relaciones y fechas sustentadas | Flechas que infieren control o coordinación no acreditada |
| ¿Por qué sube un precio? | Gráfico con ejes, unidad, periodo, fuente visible; revelar variable causal si hay evidencia | Barras bonitas con valores inventados |
| ¿Qué ve el usuario? | Recreación de interfaz respaldada por capturas oficiales o mockup explícito; cursor/scroll sincronizado | Generar app falsa que parece real |
| ¿De dónde procede el dato? | Mostrar documento primario y enfocar línea/celda concreta | Tarjeta de texto que atribuye cifras sin fuente |
| ¿Qué pasa en el tiempo? | Timeline auténtica de acontecimientos, medios originales y marcas temporales verificadas | Animación genérica que no responde al audio |
| ¿Es una conjetura del locutor? | Visual sobrio de sus premisas; indicación discreta "hipótesis" si se representa el resultado | Mostrar la especulación como algo que ya pasó |

## Ejemplos del episodio de Despegamos (15/10/2026)

**ASML y EUV**: planos auténticos de máquinas ASML y fuentes de vídeo autorizadas; para explicar el mecanismo, un corte técnico con fuente EUV → espejos reflectivos → retícula/máscara → oblea. Mostrarla como explicación simplificada, jamás como vídeo del interior de un modelo concreto. Acompañar cifras de fuentes independientes si se cuantifica coste o capacidad.

**Cartera europea de identidad**: filmaciones reales del Parlamento/Comisión y demostraciones públicas de la cartera EUDI. Si se necesita explicar la selección de credenciales, superponer una capa de UI reconocible y progresiva, basada en material oficial. No implicar que todos los historiales quedan centralizados en una única base sin evidencia.

**Euro digital**: footage BCE y terminales de pago reales. Para diferenciarlo de la cartera EUDI, composición de doble sistema con fuentes y roles correctos; indicar que son iniciativas distintas. Dibujar flujos de dinero solo si la implementación de la que se habla está documentada; las opiniones del locutor se identifican como tales.

**Google/administraciones**: imágenes reales de interlocutores y sedes correctas con fecha si procede; documento o cita verificable. No añadir banderas, candados, cámaras de seguridad ni "líneas de influencia" como si fueran prueba.

## Art direction

- 16:9, 1920x1080, 25 o 30 fps según material y master; consistentemente elegido, no 20fps.
- Contraste controlado; negros profundos sin empastar; colores reales del archivo preservados. Una o dos tintas de apoyo editoriales, sin neones por sistema.
- Tipografía funcional: fechas, nombres imprescindibles, unidades y atribución. Un rótulo cumple función, no decoración.
- Iluminación/grano/parallax/sombras reales únicamente cuando sumen integración, no como presets aplicados ciegamente.
- Movimiento con intención: reveal, rack focus simulado sobre recortes, máscara que destapa una prueba, travelling geográfico, aceleración/desaceleración naturales. No todos los elementos deben moverse.
- Composición por capas reales. Animar el *objeto que representa el concepto*, no la caja que lo contiene.
- Ritmo flexible, ajustado a la frase. Si la idea necesita 12 segundos para explicarse, permitir 12 segundos de progresión; no forzar un corte cada cuatro segundos.
- Mantener continuidad de escala/dirección entre escenas que expresan relación causal.
- Audio: conservar voces y tono; música y SFX discretos sin enmascarar contenido.

## Microguion de cada gráfico

Especificar siempre:
1. Frase y palabra gatillo con timestamps.
2. La pregunta cognitiva a responder.
3. Elementos o recursos verificables (mapa, assets reales, dataset, documento).
4. Estado inicial, 2–5 pasos de transformación y estado final.
5. Dato o conocimiento que ha quedado explicado.
6. Justificación de por qué B-roll real NO bastaba.

Si dos gráficos consecutivos muestran el mismo mecanismo de representación, sustituir el segundo por otro lenguaje visual (recorte, plano real, archivo, simulación espacial) o editar ambos como una sola explicación continua.
