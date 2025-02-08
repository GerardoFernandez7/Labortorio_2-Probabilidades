# Teoria de Probabiliades - Laboratorio 2
# Autores: 
# - Diego Patzán - 23525
# - Gerardo André Fernández Cruz - 23763
# - Anthony Lou Schwank - 23410
# - Ihan Marroquin - 23108
# - Milton Polanco - 23471
# - Roberto Nájera - 23781
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

# c) Calcular P(W): La probabilidad de agarrar una bolsa que pese por lo menos 50 g
# Contar cuántos valores cumplen la condición
cantidad_cumplec = (df["Weight"] >= 50).sum()

# e) Calcular P(T \ W): la bolsa tiene al menos 57 y pesa menos de 50 gramos
P_TW = len(df[df['Total'] >= 57 ][df["Weight"] < 50])

# Calcular la probabilidad en porcentaje
probabilidadc = cantidad_cumplec / 30
resultadoc = probabilidadc * 100

# Imprimir el resultado correctamente usando f-string
print(f"La probabilidad de elegir aleatoriamente y que la bolsa pese más de 50 es {resultadoc:.2f}%")
# Calcular la probabilidad
P_R = muestras_R / total_muestras

P_T = muestras_T / total_muestras

P_TW *= 100 / total_muestras 


print(f"Probabilidad P(R) de tener al menos 10 botonetas rojas: {P_R:.4f}")

print(f"Probabilidad P(T) de tener al menos 57 botonetas en total: {P_T:.4f}")


print(f"Probabilidad P(T\W) de tener al menos 57 botonetas en total y que pese menos de 50 gramos: {P_TW:.4f} %")
