# Teoria de Probabiliades - Laboratorio 2
# Autor: Gerardo Andre Fernandez Cruz - 23763
# Fecha: 3/2/2025

import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('MM_Data.csv')

# a) Calcular P(R): probabilidad de tener al menos 10 botonetas rojas
total_muestras = len(df)
muestras_R = len(df[df['Red'] >= 10])

# Calcular la probabilidad
P_R = muestras_R / total_muestras

print(f"Probabilidad P(R) de tener al menos 10 botonetas rojas: {P_R:.4f}")
