# Radiografía de una partida de NevWorld

Has terminado una partida y el juego ha generado un archivo JSONL. Tu misión es abrirlo con pandas y preparar una ficha que permita a otra persona comprender qué contiene ese registro.

Utiliza **los datos de tu propia partida** y las operaciones vistas en el tema. No modifiques el archivo RAW.

## Teoría de apoyo

JSONL guarda un evento en cada línea. pandas lo carga con `pd.read_json(..., lines=True)` en un **DataFrame**, una tabla de filas y columnas. La variable `df` recibe ese nombre como abreviatura de DataFrame: cada fila representa un evento y cada columna, un campo.

| Para… | Utiliza… |
| --- | --- |
| Representar y comprobar la ruta | `Path(...)` y `exists()` |
| Ver los primeros eventos | `df.head()` |
| Obtener filas y columnas | `df.shape` |
| Consultar los nombres de los campos | `df.columns.tolist()` |
| Contar eventos de cada tipo | `df['type'].value_counts()` |
| Leer un valor de la primera fila | `df['campo'].iloc[0]` |
| Obtener los extremos de los ticks | `df['tick'].min()` y `max()` |

Los eventos pueden tener campos diferentes: un `NaN` representa una ausencia, no necesariamente un error ni un cero. El tick mide tiempo simulado; varios eventos pueden compartirlo.

## Enunciado

Crea `scripts/actividades/01_radiografia.py` en tu proyecto `bigdata-game`. Carga el JSONL que has guardado en `data/raw`, comprobando antes que la ruta existe. Puedes apoyarte en el script del tema.

Aplica las cuatro validaciones básicas del tema: que la tabla no esté vacía, que existan las columnas principales, que no se repita la pareja `run_id` y `event_index`, y que los ticks no retrocedan al ordenar por `event_index`. Hazlo antes de consultar la primera fila.

Después, muestra las primeras filas y obtén los datos necesarios para completar esta ficha:

| Dato de mi partida | Resultado |
| --- | --- |
| Nombre del archivo JSONL | nevworld_708139750131559771_20261005_183106.jsonl |
| Número total de eventos | 1022 |
| Número de columnas | 34 |
| Nombres de las columnas | schema_version <br> run_id <br> seed <br> event_index <br> tick <br> type <br> started_at_utc <br> building_id <br> building_type <br> cell_x <br> cell_y <br> width <br> height <br> villager_id <br> activity <br> resource_type <br> amount_before <br> amount_after <br> amount_delta <br> population <br> constructed_buildings <br> wood_stock <br> food_stock <br> gold_stock <br> day <br> prey_type <br> actor_id <br> target_id <br> interaction_type <br> topic <br> relationship_actor_to_target_after <br> relationship_target_to_actor_after <br> need_type <br> state |
| Tipo del primer evento registrado | simulation_started |
| Tipo de evento más frecuente y cantidad | villager_activity_changed  674 |
| Recuento de todos los tipos de evento | villager_activity_changed 674 <br> resource_changed 105 <br> world_snapshot 67 <br> villager_need_changed 62 <br> social_interaction 50 <br>hunt_completed 14 <br>construction_abandoned        14 <br>villager_drank 12 <br>construction_expired 9 <br>villager_ate 8 <br>building_created 6 <br>simulation_started 1 |
| `run_id`, semilla y versión del esquema de la primera fila | 20261005_183106_708139750131559771_2ca19224b5dc4d2a8e6e7fb52ef9de55 <br> 708139750131559771 <br> 2 |
| Tick mínimo y tick máximo | 0 / 40200 |
| Resultado de las validaciones | OK |

Termina la ficha respondiendo con tus palabras:

1. ¿Qué te permite afirmar el recuento sobre tu partida? ¿Por qué el tipo más frecuente no tiene que ser el más importante?
<br>  Se han registrado 1022 eventos, con 12 tipos de eventos distintos donde el más frecuente ha sido el villager_activity_changed con 674 eventos registrados. <br> <br>No siempre debe implicar que mayor frecuencia sea un motivo de analisis, por ejemplo: puede indicar que simplemente que ser realizan correctamente las acciones. <br><br>
2. ¿Por qué una celda vacía no significa necesariamente que el registro esté mal?
<br> Pueden existir columnas que almacenan datos para unos eventos en concreto pero que no son necesarios para otros. <br><br>
3. ¿Qué sabes ahora del archivo y qué pregunta sobre tu partida necesitaría un análisis posterior?
<br> Sabemos que contiene la estructura básica para poder ser analizado y que inicialmente no hay errores como que el fichero no se encuentra, contienen las columnas esenciales, no existen duplicados y que no hay fallo a la hora de generar los ticks.

Para esta partida, habría que analizar por qué han abandonado las construcciones.

Podemos abrir, reconocer eventos y comprobar que tienen la estructura básica para poder ser utilizado. 

Ejecuta desde la raíz de `bigdata-game`, con el entorno de Python que tenga pandas instalado:

```powershell
python scripts/actividades/01_radiografia.py
```

**Entrega:** Cread un repositorio en Github con una carpeta llamada NevWorld, y una subcarpeta llamada fase01, en la que incluiréis el script y la ficha en un archivo de texto, con tus respuestas y resultados reales. Si alguna validación falla, anota el error y explica qué comprobación no se cumple; no alteres el RAW para hacerla pasar.