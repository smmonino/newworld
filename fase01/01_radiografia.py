from pathlib import Path

import pandas as pd


DATASET = Path('data/raw/nevworld_708139750131559771_20261005_183106.jsonl')
if not DATASET.exists():
    raise FileNotFoundError(f'No se encuentra: {DATASET.resolve()}')
df = pd.read_json(DATASET, lines = True)

def validacion_dataset(df):
    required = ['run_id', 'event_index', 'tick', 'type']
    
    assert not df.empty, 'El dataset está vacío'
    
    assert all (column in df.columns for column in required), 'Faltan columnas principales'
    
    assert not df.duplicated(['run_id', 'event_index']).any(), 'Hay eventos duplicados'
    
    ordered = df.sort_values('event_index')
    assert ordered['tick'].is_monotonic_increasing, 'Los ticks retroceden'
    
    print('VALIDACIÓN INICIAL: OK')


def obtener_datos(df, DATASET):
    print('\n\n PRIMEROS EVENTOS: ')
    print(df.head())

    print('Nombre del archivo JSONL: ', DATASET.name)
    
    filas, columnas = df.shape
    print('Número total de eventos: ', filas)
    
    print('Número total de columnas: ', columnas)
    
    print('Nombres de las columnas: ', df.columns.tolist())
    
    print('Tipo del primer evento registrado: ', df['type'].iloc[0])
    
    print('Tipo del evento más frecuente y cantidad: ', df['type'].value_counts().index[0], '-', df['type'].value_counts().iloc[0])
    
    print('Recuento de todos los tipos de evento: ', df['type'].value_counts())
    
    print('run_id, semilla y versión del esquema de la primera fila: ', df['run_id'].iloc[0], '-', df['seed'].iloc[0], '-', df['schema_version'].iloc[0])
    
    print('Tick mínimo y tick máximo: ', df['tick'].min(), '/', df['tick'].max())
    
    print('Resultado de las validaciones: ')
    
    
validacion_dataset(df)
obtener_datos(df, DATASET)
