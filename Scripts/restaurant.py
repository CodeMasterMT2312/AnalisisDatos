import pandas as pd

# Cargar el dataset
df = pd.read_csv('../Restaurant/Restaurant reviews.csv')

# Verificar las primeras filas y la información del dataset
print("Primeras 5 filas del dataset original:")
print(df.head())

print("\nResumen del dataset original:")
print(df.info())

print("\nEstadísticas descriptivas del dataset original:")
print(df.describe())

# Eliminar columnas no deseadas (asegúrate de que los nombres de las columnas son correctos)
columns_to_drop = ['7514', 'Pictures']
for column in columns_to_drop:
    if column in df.columns:
        df = df.drop(columns=[column])
    else:
        print(f"Columna {column} no encontrada en el dataset.")

# Filtrar filas con valores no numéricos en la columna 'Rating'
def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

df = df[df['Rating'].apply(is_numeric)]

# Convertir columna 'Rating' a tipo float
df['Rating'] = df['Rating'].astype(float)

# Convertir columna 'Time' a tipo datetime
df['Time'] = pd.to_datetime(df['Time'])

# Renombrar columnas
df = df.rename(columns={
    'Restaurant': 'Restaurante',
    'Reviewer': 'Critico',
    'Rating': 'Valoracion',
    'time': 'tiempo'
})

# Verificar los tipos de datos después de la conversión
print("\nTipos de datos después de la conversión:")
print(df.dtypes)

# Verificar las primeras filas del dataset limpio
print("\nPrimeras 5 filas del dataset limpio:")
print(df.head())

# Guardar el dataset limpio en un nuevo archivo CSV
df.to_csv('../Restaurant/Restaurant_reviews_Clean.csv', index=False)

# Verificar que el archivo CSV se ha escrito correctamente
print("\nEl archivo CSV limpio se ha guardado correctamente.")
