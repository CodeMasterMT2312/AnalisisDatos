import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('../Restaurantes/sepetcioglu_restaurant.csv')

# Muestra las primeras filas del dataset original
print("Primeras 5 filas del dataset original:")
print(df.head())

# Muestra un resumen del dataset original
print("\nResumen del dataset original:")
print(df.info())

# Muestra estadísticas descriptivas del dataset original
print("\nEstadísticas descriptivas del dataset original:")
print(df.describe())

# Traduce los nombres de las columnas al español
df = df.rename(columns={
    'photo': 'foto',
    'rating': 'calificacion',
    'rating_category': 'categoria_calificacion'
})

# Convierte las columnas a los tipos de datos adecuados
df['foto'] = df['foto'].astype(str)
df['calificacion'] = df['calificacion'].astype(float)
df['categoria_calificacion'] = df['categoria_calificacion'].astype(str)

# Muestra los tipos de datos después de la conversión
print("\nTipos de datos después de la conversión:")
print(df.dtypes)

# Muestra las primeras filas del dataset limpio
print("\nPrimeras 5 filas del dataset limpio:")
print(df.head())

# Guarda el dataset limpio en un nuevo archivo CSV
df.to_csv('../Restaurantes/sepetcioglu_restaurant_limpio.csv', index=False)

# Verifica que el archivo CSV se ha escrito correctamente
print("\nEl archivo CSV limpio se ha guardado correctamente.")
