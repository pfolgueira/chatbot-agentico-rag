"""Genera varios PDFs de ejemplo dentro de la carpeta `datos/`.

Se crean 4 documentos sobre fútbol con nombres claros.
"""

from pathlib import Path

from fpdf import FPDF


OUT_DIR = Path(__file__).resolve().parent.parent / "datos"

DOCUMENTS = [
    ("futbol_intro.pdf", """
INTELIGENCIA DEPORTIVA: EL FÚTBOL COMO FENÓMENO GLOBAL

1. ORÍGENES Y EVOLUCIÓN HISTÓRICA
El fútbol no nació de la nada; es el resultado de siglos de evolución de juegos de pelota. Mientras que el "Cuju" en la antigua China (siglo III a.C.) es reconocido por la FIFA como la forma más antigua de fútbol, no fue hasta el siglo XIX en las escuelas públicas del Reino Unido donde el caos se transformó en orden. 

En 1848, las "Reglas de Cambridge" intentaron unificar los criterios de juego, pero el hito definitivo ocurrió en 1863 en la Taberna Freemasons de Londres, con la creación de la Football Association (FA). Este momento marcó la separación definitiva entre el fútbol y el rugby, prohibiendo el uso de las manos para desplazar el balón. Desde entonces, el deporte se expandió a través de las rutas comerciales británicas, llegando a Sudamérica y al resto de Europa a finales del siglo XIX.

2. REGLAMENTACIÓN Y DINÁMICA DEL JUEGO
El fútbol moderno se rige por 17 reglas básicas, mantenidas por la International Football Association Board (IFAB). Un partido estándar consta de dos tiempos de 45 minutos. El objetivo parece simple —marcar más goles que el oponente—, pero la complejidad reside en la gestión del espacio y el tiempo.

La regla del "fuera de juego" (offside) es quizás el elemento táctico más importante, ya que evita que los atacantes se queden esperando cerca de la portería contraria, obligando a los equipos a construir el juego de forma colectiva y dinámica. Además, la figura del árbitro y sus asistentes asegura que el "fair play" se mantenga, utilizando tarjetas amarillas y rojas para sancionar conductas antideportivas.

3. LA ESTRUCTURA DEL CAMPO Y LAS POSICIONES
Un terreno de juego reglamentario debe tener entre 90 y 120 metros de largo. En este espacio, los once jugadores de cada equipo se desplazan siguiendo roles específicos:
- El Guardameta: El único con el privilegio de usar las manos, es la última línea de defensa.
- Los Defensas: Centrales y laterales que buscan proteger su área y dar salida al balón.
- Los Centrocampistas: El motor del equipo. Se dividen en pivotes defensivos, creadores de juego y mediapuntas.
- Los Delanteros: Especialistas en la finalización y la presión alta.

4. EL FÚTBOL COMO MOTOR ECONÓMICO Y SOCIAL
Hoy en día, el fútbol trasciende las líneas de cal. Se ha convertido en una industria multimillonaria que representa un porcentaje significativo del PIB en países como España, Inglaterra o Brasil. Los derechos televisivos, el patrocinio técnico y el mercado de fichajes mueven cifras astronómicas cada año.

Socialmente, el fútbol funciona como un lenguaje universal. Es capaz de detener guerras (como se ha visto en casos históricos en África) o de unir a naciones enteras bajo una sola bandera durante la Copa Mundial de la FIFA. La identidad cultural de muchas ciudades está intrínsecamente ligada a sus clubes locales, generando un sentido de pertenencia que pasa de generación en generación.

5. INNOVACIÓN Y TECNOLOGÍA: EL VAR Y MÁS ALLÁ
En la última década, el fútbol ha abrazado la tecnología para reducir el error humano. El VAR (Video Assistant Referee) ha transformado la justicia en el juego, aunque no sin polémica. A esto se suma el uso de "Big Data" y dispositivos GPS que los jugadores llevan bajo sus camisetas para medir el rendimiento físico en tiempo real. 

La Inteligencia Artificial ahora predice probabilidades de gol (Expected Goals - xG) y ayuda a los ojeadores a encontrar talentos en ligas remotas analizando miles de variables estadísticas, demostrando que el deporte rey es ahora una ciencia exacta.

6. DESAFÍOS Y FUTURO
El futuro del fútbol se enfrenta a retos como la sostenibilidad financiera de los clubes, la creación de nuevas competiciones (como la propuesta Superliga) y la necesidad de mantener el interés de las nuevas generaciones que consumen contenido de forma más fragmentada. Sin embargo, mientras haya un balón y dos piedras que sirvan de portería en un patio de colegio, la esencia del fútbol permanecerá intacta.
""".strip()),

    ("futbol_tactica.pdf", """
ANÁLISIS TÁCTICO: EL AJEDREZ DEL CÉSPED

1. LA EVOLUCIÓN DE LOS SISTEMAS DE JUEGO
La táctica en el fútbol ha recorrido un largo camino desde el siglo XIX. En los inicios del deporte, la prioridad era el ataque desmesurado, utilizándose formaciones como el 1-2-7, donde siete delanteros buscaban el gol sin apenas rigor defensivo. Fue Herbert Chapman, con su famosa "WM" (3-2-2-3), quien introdujo el equilibrio entre las líneas.

Posteriormente, Brasil popularizó el 4-2-4 en 1958, que evolucionó hacia el clásico 4-4-2, el sistema más equilibrado y utilizado durante décadas. Hoy en día, vivimos en la era de la flexibilidad táctica, donde un equipo puede atacar en un 3-4-3 y defender en un 5-4-1, adaptándose a la posición del balón y del rival en tiempo real.

2. ROLES ESPECÍFICOS Y LA REVOLUCIÓN DE LAS POSICIONES
El fútbol moderno ha desdibujado las fronteras entre las posiciones tradicionales, exigiendo jugadores polivalentes:

- El Portero Líbero: Ya no basta con detener balones. Porteros como Manuel Neuer o Ederson funcionan como el primer atacante, iniciando el juego con pases precisos de larga distancia y saliendo de su área para cortar avances rivales.
- Centrales de Salida: Los defensores centrales modernos deben poseer una técnica depurada para romper líneas de presión mediante conducciones o pases filtrados.
- Laterales Invertidos e Interiores: Popularizados por entrenadores como Pep Guardiola, estos laterales no corren por la banda, sino que se sitúan en el centro del campo para generar superioridad numérica y control de la posesión.
- El Falso Nueve: Un delantero que abandona el área para asociarse con los centrocampistas, arrastrando a los defensas centrales y creando espacios para que los extremos ataquen el interior.

3. LAS CUATRO FASES DEL JUEGO
Para entender la táctica, debemos dividir el partido en cuatro momentos críticos:
- Ataque Organizado: Cuando el equipo tiene el balón contra una defensa asentada. Aquí prima la amplitud (abrir el campo) y la profundidad.
- Transición Defensiva (Tras pérdida): El momento en que se pierde el balón. Los equipos modernos suelen aplicar el "Gegenpressing" o presión tras pérdida inmediata para recuperar el esférico en menos de 5 segundos.
- Defensa Organizada: El equipo se repliega. Puede optar por una "presión alta" (bloque alto) para forzar el error en campo rival, o un "bloque bajo" (cerrojo) para proteger el área y salir al contraataque.
- Transición Ofensiva (Contraataque): La velocidad es clave. Se busca aprovechar el desorden defensivo del rival que acaba de perder el balón para llegar al arco en el menor número de toques posible.

4. EL USO DEL ESPACIO: PASILLOS INTERIORES Y AMPLITUD
El campo se divide teóricamente en cinco pasillos verticales: dos bandas, dos carriles interiores (conocidos como "half-spaces") y un carril central. La táctica de élite se centra en ocupar los carriles interiores, ya que desde ahí un jugador tiene un ángulo de visión y de pase mucho más peligroso que desde la banda. 

El concepto de "Tercer Hombre" es otra herramienta táctica fundamental: el jugador A quiere pasar al jugador C, pero el camino está bloqueado; por tanto, pasa al jugador B, quien de primera descarga hacia el jugador C, que ahora está libre de marca.

5. PREPARACIÓN ESTRATÉGICA Y EL BALÓN PARADO
Casi el 30% de los goles en el fútbol profesional provienen de acciones a balón parado (córners, faltas laterales, penaltis). Esto ha llevado a la creación de la figura del "entrenador de jugadas ensayadas". La táctica aquí es pura pizarra: bloqueos, pantallas y movimientos de distracción que buscan liberar a un rematador en una zona específica del área pequeña.

6. PSICOLOGÍA Y TÁCTICA
Finalmente, la táctica no es solo física y técnica; es mental. Un sistema táctico falla si los jugadores no creen en él o si no tienen la resistencia cognitiva para mantener la concentración durante los 90 minutos. La disciplina táctica permite que equipos con menor talento individual superen a gigantes mediante el orden, el sacrificio colectivo y el cierre de espacios.
""".strip()),

    ("mundial_historia.pdf",
    """
LA COPA MUNDIAL DE LA FIFA: EL MAYOR ESPECTÁCULO DE LA TIERRA

1. EL NACIMIENTO DE UN SUEÑO (1930)
La historia del Mundial comenzó con la visión de Jules Rimet, quien impulsó la creación de un torneo que uniera a las naciones a través del fútbol profesional, fuera de los Juegos Olímpicos. En 1930, Uruguay fue elegida como sede no solo por ser la vigente campeona olímpica, sino por celebrar el centenario de su independencia. 

Aquel primer torneo fue una odisea: las selecciones europeas tuvieron que cruzar el Atlántico en barco durante semanas para participar. Solo 13 naciones compitieron, y Uruguay se consagró primer campeón al vencer a Argentina 4-2 en el Estadio Centenario. Este hito sentó las bases de una competición que se repetiría cada cuatro años, con las excepciones de 1942 y 1946 debido a la Segunda Guerra Mundial.

2. LA ERA DE ORO Y EL SURGIMIENTO DE LAS LEYENDAS
Tras la guerra, el Mundial se convirtió en el escenario donde se forjaron los mitos más grandes del deporte:

- El Maracanazo (1950): Un momento que cambió la psicología del fútbol brasileño, cuando Uruguay derrotó a Brasil en un estadio con 200,000 personas.
- El Reinado de Pelé: Edson Arantes do Nascimento, "Pelé", es el único jugador en la historia en ganar tres Mundiales (1958, 1962, 1970). Su Brasil de 1970 es considerado por muchos como el mejor equipo de todos los tiempos, una oda al "fútbol arte".
- La Mano de Dios y el Siglo (1986): Diego Armando Maradona protagonizó en México 86 el partido más icónico de la historia contra Inglaterra, marcando un gol con la mano y, minutos después, el "Gol del Siglo" tras regatear a medio equipo rival.

3. EL CLUB EXCLUSIVO DE LOS CAMPEONES
A pesar de que cientos de naciones compiten en las eliminatorias, solo ocho han logrado tocar la gloria. La jerarquía mundial se reparte así:
- Brasil (5): Los "Pentacampeões", sinónimo de magia y talento.
- Alemania e Italia (4 cada uno): Ejemplos de rigor táctico, resiliencia y competitividad extrema.
- Argentina (3): La actual campeona, que alcanzó su tercera estrella en 2022 de la mano de Lionel Messi en la que muchos consideran la mejor final de la historia.
- Francia y Uruguay (2 cada uno): Francia como la potencia moderna de formación de talento y Uruguay como el pionero histórico.
- Inglaterra y España (1 cada uno): Naciones con las ligas más potentes que lograron coronar su historia con los títulos de 1966 y 2010 respectivamente.

4. EVOLUCIÓN DEL FORMATO Y TECNOLOGÍA
El torneo ha mutado para adaptarse a un mundo globalizado. De los 13 equipos de 1930, pasamos a 16 durante gran parte del siglo XX, luego a 24 en España 1982, y a 32 en Francia 1998. El próximo gran salto ocurrirá en 2026 (Norteamérica), donde 48 selecciones buscarán la copa, abriendo las puertas a más naciones de África y Asia.

La tecnología también ha reclamado su lugar. Desde el primer balón de cuero con costuras externas hasta el "Al Rihla" de 2022 con sensores de movimiento integrados. La implementación del VAR y la tecnología de línea de gol han buscado eliminar las injusticias históricas, aunque el debate sobre la esencia del juego continúa vivo en cada bar y grada del mundo.

5. IMPACTO SOCIOECONÓMICO Y CULTURAL
Un Mundial es más que fútbol; es una herramienta geopolítica. Ser sede implica una inversión masiva en infraestructura y estadios que transforman ciudades enteras. Para el espectador, el Mundial es un rito de paso: recordamos dónde estábamos en cada final, quién nos acompañaba y cómo celebramos o lloramos. 

Las canciones oficiales, las mascotas y las innovaciones en las retransmisiones televisivas han convertido al Mundial en un producto cultural consumido por más de 3,500 millones de personas. Es el único evento capaz de detener la productividad de un país entero durante 90 minutos.

6. HACIA EL FUTURO: EL MUNDIAL DE 2026 Y MÁS ALLÁ
El futuro plantea desafíos logísticos inmensos. El torneo de 2026 será el primero organizado por tres países simultáneamente (EE.UU., México y Canadá). La sostenibilidad ambiental y la ética en la elección de las sedes son los nuevos pilares que la FIFA debe gestionar para asegurar que el torneo siga siendo el símbolo de unidad y excelencia que Jules Rimet soñó hace casi un siglo.
""".strip()),

    ("futbol_femenino.pdf", """
EL AUGE DEL FÚTBOL FEMENINO: ROMPIENDO EL TECHO DE CRISTAL

1. LOS CIMIENTOS Y LAS PROHIBICIONES HISTÓRICAS
Aunque hoy disfrutamos de estadios llenos, el camino del fútbol femenino estuvo marcado por la resistencia. A finales del siglo XIX y principios del XX, el fútbol femenino gozaba de una popularidad sorprendente, especialmente en Inglaterra durante la Primera Guerra Mundial con equipos como el "Dick, Kerr Ladies". Sin embargo, en 1921, la FA prohibió el fútbol femenino en sus campos alegando que el deporte era "inadecuado para las mujeres".

Esta prohibición, que duró 50 años en Inglaterra y se replicó en países como Alemania y Brasil, frenó drásticamente el desarrollo de la disciplina. No fue hasta la década de 1970 cuando las federaciones comenzaron a levantar los vetos, iniciando un lento proceso de reconstrucción que culminaría en la primera Copa del Mundo oficial de la FIFA en 1991, celebrada en China.

2. EL PUNTO DE INFLEXIÓN: PROFESIONALIZACIÓN Y VISIBILIDAD
La última década ha sido testigo de un cambio de paradigma. La transición del semiprofesionalismo a ligas totalmente profesionales ha elevado el nivel táctico y físico del juego. Ligas como la Liga F (España), la WSL (Inglaterra) y la NWSL (Estados Unidos) han establecido estándares de entrenamiento, salarios y servicios médicos que antes eran impensables.

El apoyo de los clubes de élite masculinos, que han integrado secciones femeninas con infraestructuras de primer nivel, ha sido clave. El FC Barcelona Femení, por ejemplo, se ha convertido en un referente mundial no solo por sus títulos, sino por su capacidad de atraer a más de 90,000 espectadores al Camp Nou, rompiendo récords mundiales de asistencia de forma consecutiva.

3. ICONOS GLOBALES Y EL PODER DE LA REPRESENTACIÓN
El fútbol femenino ha generado sus propias leyendas, cuyas voces trascienden el campo de juego:
- Marta Vieira da Silva: La "Reina" brasileña, máxima goleadora en la historia de los Mundiales (superando incluso los registros masculinos), ha sido la cara del talento puro durante dos décadas.
- Megan Rapinoe: Un icono de la lucha por la igualdad salarial y los derechos civiles, demostrando que la futbolista moderna tiene un rol social activo.
- Alexia Putellas: Primera jugadora en ganar dos Balones de Oro de forma consecutiva, simbolizando la excelencia técnica y el auge del fútbol europeo.

Estas figuras han servido de espejo para millones de niñas, quienes ahora ven en el fútbol una carrera profesional legítima y aspiracional.

4. EL ÉXITO DE LOS GRANDES TORNEOS
La Copa Mundial Femenina de 2023 en Australia y Nueva Zelanda marcó un antes y un después. Con una audiencia global que superó los 2,000 millones de espectadores y estadios con el cartel de "no hay billetes", el torneo demostró que el fútbol femenino es un producto comercialmente viable y extremadamente atractivo. La competitividad ha aumentado, con selecciones de todos los continentes reduciendo la brecha con las potencias tradicionales como Estados Unidos.

5. DESAFÍOS: LA LUCHA POR LA EQUIDAD
A pesar del éxito, el camino hacia la equidad total sigue presentando retos. La brecha salarial, la diferencia en los presupuestos de marketing y la necesidad de más mujeres en puestos directivos dentro de las federaciones son las batallas actuales. El concepto de "Equal Pay" (igualdad de pago), implementado ya en selecciones como la estadounidense o la noruega, es el objetivo hacia el que se dirige la industria global.

6. UN FUTURO SIN LÍMITES
El fútbol femenino no es una moda, sino un movimiento consolidado. Con la inversión creciente de patrocinadores globales y el aumento de la cobertura mediática, el futuro es brillante. La integración de tecnologías como el análisis de datos específico para la fisiología femenina y el desarrollo de academias juveniles exclusivas garantizan que el talento seguirá brotando. El fútbol, finalmente, está cumpliendo su promesa de ser un deporte para todos.
""".strip()),
]


def _write_pdf(path: Path, content: str) -> None:
    def _sanitize(text: str) -> str:
        # Replace some Unicode punctuation not supported by default PDF core fonts
        replacements = {
            "\u2014": "-",  # em dash
            "\u2013": "-",  # en dash
            "\u2018": "'",  # left single quote
            "\u2019": "'",  # right single quote
            "\u201c": '"',  # left double quote
            "\u201d": '"',  # right double quote
            "\u2010": '-',
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=12)
    # Use sanitized text to avoid encoding errors with core fonts
    safe_text = _sanitize(content)
    pdf.multi_cell(0, 7, safe_text)
    pdf.output(str(path))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for fname, text in DOCUMENTS:
        out_path = OUT_DIR / fname
        _write_pdf(out_path, text)
        print(f"PDF generado: {out_path}")


if __name__ == "__main__":
    main()