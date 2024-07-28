import pandas as pd

# Paso 1: Cargar el dataset CSV
file_path = '../Sport/athlete_events.csv'
df = pd.read_csv(file_path)

# Paso 2: Exploración inicial del dataset
print("Primeras 5 filas del dataset original:\n", df.head())
print("\nResumen del dataset original:\n", df.info())
print("\nEstadísticas descriptivas del dataset original:\n", df.describe())

# Paso 3: Limpieza de datos

# Eliminar valores nulos
df = df.dropna()

# Convertir tipos de datos (si es necesario)
# Asegúrate de que las columnas tienen el tipo de dato correcto
df['ID'] = df['ID'].astype(int)
df['Name'] = df['Name'].astype(str)
df['Sex'] = df['Sex'].astype(str)
df['Age'] = df['Age'].astype(int)
df['Height'] = df['Height'].astype(float)
df['Weight'] = df['Weight'].astype(float)
df['Team'] = df['Team'].astype(str)
df['NOC'] = df['NOC'].astype(str)
df['Games'] = df['Games'].astype(str)
df['Year'] = df['Year'].astype(int)
df['Season'] = df['Season'].astype(str)
df['City'] = df['City'].astype(str)
df['Sport'] = df['Sport'].astype(str)
df['Event'] = df['Event'].astype(str)
df['Medal'] = df['Medal'].astype(str)

# Eliminar duplicados
df = df.drop_duplicates()

# Paso 4: Guardar el dataset limpio

# Guardar como CSV
cleaned_file_path_csv = '../Sport/athlete_events_cleaned_file.csv' 
df.to_csv(cleaned_file_path_csv, index=False)

print("\nEl dataset limpio se ha guardado correctamente.")
