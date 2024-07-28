import pandas as pd

df = pd.read_csv('../Sport/goalscorers.csv')

print(df.head())  # Muestra las primeras 5 filas
print(df.info())  # Muestra un resumen del dataset
print(df.describe())  # Muestra estadísticas descriptivas
df = df.dropna()
df = df.drop_duplicates()
df = df.rename(columns={'own_goal': 'Auto_Gol'})
df = df.rename(columns={'penalty': 'Penales'})
df = df.rename(columns={'minute': 'Minuto'})
df = df.rename(columns={'scorer': 'goleador'})
df = df.rename(columns={'team': 'Equipo'})
df = df.rename(columns={'away_team': 'Equipo_Visitante'})
df = df.rename(columns={'date': 'Fecha'})
df = df.rename(columns={'home_team': 'Equipo_Local'})

df.to_csv('../Sport/goalscorersClean.csv', index=False)


