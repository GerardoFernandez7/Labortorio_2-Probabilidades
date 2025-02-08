# Teoria de Probabiliades - Laboratorio 2
# Autores: 
# - Diego Patzán - 23525
# - Gerardo André Fernández Cruz - 23763
# - Anthony Lou Schwank - 23410
# - Ihan Marroquin - 23108
# - Milton Polanco - 23471
# - Roberto Nájera - 23781
# Fecha: 3/2/2025

# Probabilidades dadas en el problema
probabilidad_enfermedad = 1 / 100000  # P(E)
probabilidad_no_enfermedad = 1 - probabilidad_enfermedad  # P(¬E)
sensibilidad = 0.95  # P(Positivo|E)
falso_positivo = 1e-3  # P(Positivo|¬E)

probabilidades = {
    "enfermedad": [probabilidad_enfermedad, probabilidad_no_enfermedad],  # P(E) y P(¬E)
    "positivo_dado_enfermedad": [sensibilidad, 1 - sensibilidad],  # P(Positivo|E) y P(Negativo|E)
    "positivo_dado_no_enfermedad": [falso_positivo, 1 - falso_positivo]  # P(Positivo|¬E) y P(Negativo|¬E)
}

# Mostrar las listas de probabilidades
print("-------------------- Listas de Probabilidades ----------------------")
print("Probabilidades de enfermedad: P(E), P(¬E) ->", probabilidades["enfermedad"])
print("Probabilidades dado que tiene la enfermedad: P(Positivo|E), P(Negativo|E) ->", probabilidades["positivo_dado_enfermedad"])
print("Probabilidades dado que no tiene la enfermedad: P(Positivo|¬E), P(Negativo|¬E) ->", probabilidades["positivo_dado_no_enfermedad"])

# Aplicando el Teorema de Bayes: P(E|Positivo) = [P(Positivo|E) * P(E)] / P(Positivo)
# Donde: P(Positivo) = P(Positivo|E)*P(E) + P(Positivo|¬E)*P(¬E)

# Cálculo de P(Positivo)
probabilidad_positivo = (sensibilidad * probabilidad_enfermedad) + (falso_positivo * probabilidad_no_enfermedad)

# Cálculo de P(E|Positivo)
probabilidad_enfermedad_dado_positivo = (sensibilidad * probabilidad_enfermedad) / probabilidad_positivo


# Resultados
print(".")
print("------------------------- Resultados -------------------------------")
print(f"Probabilidad de tener la enfermedad (P(E)): {probabilidad_enfermedad * 100:.3f}%")
print(f"Probabilidad de no tener la enfermedad (P(\u00ACE)): {probabilidad_no_enfermedad * 100:.3f}%")
print(f"Probabilidad de obtener un resultado positivo (P(Positivo)): {probabilidad_positivo * 100:.3f}%")
print(f"Probabilidad de tener la enfermedad dado un resultado positivo (P(E|Positivo)): {probabilidad_enfermedad_dado_positivo * 100:.3f}%")
print("La probabilidad de tener la enfermedad dado que la prueba es positiva es aproximadamente 0.94%")
