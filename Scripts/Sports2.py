import pandas as pd

# Paso 1: Cargar el dataset CSV
file_path = '../Sport/Olympic_Athlete_Event_Results.csv'  # Cambia esto por la ruta de tu archivo CSV
df = pd.read_csv(file_path)

# Paso 2: Exploración inicial del dataset
print("Primeras 5 filas del dataset original:\n", df.head())
print("\nResumen del dataset original:\n", df.info())
print("\nEstadísticas descriptivas del dataset original:\n", df.describe(include='all'))

# Paso 3: Limpieza de datos

# Eliminar valores nulos en columnas críticas si es necesario
df = df.dropna(subset=['edition', 'edition_id', 'country_noc', 'sport', 'event', 'result_id', 'athlete', 'athlete_id', 'pos', 'isTeamSport'])

# Convertir tipos de datos (si es necesario)
df['edition'] = df['edition'].astype(str)
df['edition_id'] = df['edition_id'].astype(int)
df['country_noc'] = df['country_noc'].astype(str)
df['sport'] = df['sport'].astype(str)
df['event'] = df['event'].astype(str)
df['result_id'] = df['result_id'].astype(int)
df['athlete'] = df['athlete'].astype(str)
df['athlete_id'] = df['athlete_id'].astype(int)
df['pos'] = df['pos'].astype(str)  # Consider using a categorical type if appropriate
df['medal'] = df['medal'].astype(str)
df['isTeamSport'] = df['isTeamSport'].astype(bool)

# Eliminar duplicados
df = df.drop_duplicates()

# Paso 4: Guardar el dataset limpio

# Guardar como CSV
cleaned_file_path_csv = '../Sport/Olympic_Athlete_Event_Results_cleaned_file.csv'  # Cambia esto por la ruta donde deseas guardar el archivo limpio
df.to_csv(cleaned_file_path_csv, index=False)

print("\nEl dataset limpio se ha guardado correctamente.")
