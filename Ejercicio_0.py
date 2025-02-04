# Teoria de Probabiliades - Laboratorio 2
# Autor: Gerardo Andre Fernandez Cruz - 23763
# Fecha: 3/2/2025

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('MM_Data.csv')

# a) Calcular P(R): probabilidad de tener al menos 10 botonetas rojas
total_muestras = len(df)
muestras_R = len(df[df['Red'] >= 10])

# b) Calcular P(T): probabilidad de tener al menos 57 botonetas en total
# Sumar todas las columnas de colores para obtener el total de botonetas por muestra
df['Total'] = df[['Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Brown']].sum(axis=1)


# Filtrar las muestras que cumplen con el evento T (al menos 57 botonetas en total)
muestras_T = len(df[df['Total'] >= 57])

# Calcular la probabilidad
P_R = muestras_R / total_muestras

P_T = muestras_T / total_muestras



print(f"Probabilidad P(R) de tener al menos 10 botonetas rojas: {P_R:.4f}")

print(f"Probabilidad P(T) de tener al menos 57 botonetas en total: {P_T:.4f}")
