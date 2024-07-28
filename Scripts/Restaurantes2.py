import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('../Restaurantes/reviews.csv')

# Muestra las primeras filas del dataset original
print("Primeras 5 filas del dataset original:")
print(df.head())

# Muestra un resumen del dataset original
print("\nResumen del dataset original:")
print(df.info())

# Muestra estadísticas descriptivas del dataset original
print("\nEstadísticas descriptivas del dataset original:")
print(df.describe())

# Elimina duplicados y valores nulos
df = df.drop_duplicates()
df = df.dropna()

# Elimina la columna 'photo'
df = df.drop(columns=['photo'])

# Traduce los nombres de las columnas al español
df = df.rename(columns={
    'business_name': 'nombre_negocio',
    'author_name': 'nombre_autor',
    'text': 'texto',
    'rating': 'calificacion',
    'rating_category': 'categoria_calificacion'
})

# Convierte las columnas a los tipos de datos adecuados
df['nombre_negocio'] = df['nombre_negocio'].astype(str)
df['nombre_autor'] = df['nombre_autor'].astype(str)
df['texto'] = df['texto'].astype(str)
df['calificacion'] = df['calificacion'].astype(float)
df['categoria_calificacion'] = df['categoria_calificacion'].astype(str)

# Muestra los tipos de datos después de la conversión
print("\nTipos de datos después de la conversión:")
print(df.dtypes)

# Muestra las primeras filas del dataset limpio
print("\nPrimeras 5 filas del dataset limpio:")
print(df.head())

# Guarda el dataset limpio en un nuevo archivo CSV
df.to_csv('../Restaurantes/reviews_limpio.csv', index=False)

# Verifica que el archivo CSV se ha escrito correctamente
print("\nEl archivo CSV limpio se ha guardado correctamente.")
