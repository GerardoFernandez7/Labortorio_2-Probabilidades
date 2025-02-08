# Teoria de Probabiliades - Laboratorio 2
# Autores: 
# - Diego Patzán - 23525
# - Gerardo André Fernández Cruz - 23763
# - Anthony Lou Schwank - 23410
# - Ihan Marroquin - 23108
# - Milton Polanco - 23471
# - Roberto Nájera - 23781
# Fecha: 3/2/2025

# Probabilidades dadas
pu = [1/3, 1/3, 1/3]  # Probabilidad de cada urna
pl_u = [1/2, 2/5, 1/3]  # P(L|U=i)
pt_lyu = [2/3, 1/2, 2/5]  # P(T|L,U=i)

# a) Calcular P(L ∩ T) usando el teorema de probabilidad total
p_l_y_t = 0
for i in range(3):
    p_l_y_t += pu[i] * pl_u[i] * pt_lyu[i]

print(f"La probabilidad de que la dona sea de limón y en forma de toro es: {p_l_y_t:.4f}")

# Mostrar el cálculo paso a paso    
print("\nCálculo paso a paso (inciso a):")
for i in range(3):
    prob_urna = pu[i] * pl_u[i] * pt_lyu[i]
    print(f"Urna {i}: P(U={i}) * P(L|U={i}) * P(T|L,U={i}) = {pu[i]:.4f} * {pl_u[i]:.4f} * {pt_lyu[i]:.4f} = {prob_urna:.4f}")

# b) Calcular P(U=2 | L ∩ T) usando el teorema de Bayes
# P(U=2 | L ∩ T) = [P(U=2) * P(L|U=2) * P(T|L,U=2)] / P(L ∩ T)

# Numerador: P(U=2) * P(L|U=2) * P(T|L,U=2)
numerador = pu[2] * pl_u[2] * pt_lyu[2]

# Denominador: P(L ∩ T) ya calculado en el inciso a)
denominador = p_l_y_t

# Calcular la probabilidad usando la fórmula de Bayes
p_u2_dado_l_y_t = numerador / denominador

print(f"\nLa probabilidad de que la dona provenga de la urna 2 dado que es de limón y en forma de toro es: {p_u2_dado_l_y_t:.4f}")

# c) Calcular P(U=1 | L ∩ T) 
#Sabiendo que la probabilidad de agarrar cualquier urna es 1/3
#La probabilidad de agarrar una donda de limon dada cualquier urna esta dada por 1/2, 2/5, 1/3 respectivo al numero de la urna
#Y sabiendo que la probabilidad que tenga forma de toro dado a que es de limon es 2/3, 1/2, 2/5 respectivo al numero de la urna

probabilidadc = 1/3*2/5*1/2
resultadoc = probabilidadc * 100
print(f"La probabilidad de elegir aleatoriamente y que me salga una dona de limon con forma de toro en la Urna 1 es {resultadoc:.2f}%")


# Mostrar el cálculo paso a paso
print("\nCálculo paso a paso (inciso b):")
print(f"Numerador = P(U=2) * P(L|U=2) * P(T|L,U=2) = {pu[2]:.4f} * {pl_u[2]:.4f} * {pt_lyu[2]:.4f} = {numerador:.4f}")
print(f"Denominador = P(L ∩ T) = {denominador:.4f}")
print(f"P(U=2 | L ∩ T) = {numerador:.4f} / {denominador:.4f} = {p_u2_dado_l_y_t:.4f}")


# d) Calcular probabilidad de que la dona sea de la urna 0 dado que es de limón y con forma de toro
# Numerador: P(U=0) * P(L|U=0) * P(T|L,U=0)
numerador = pu[0] * pl_u[0] * pt_lyu[0]

# Denominador: P(L ∩ T) ya calculado en el inciso a)
denominador = p_l_y_t

# Calcular la probabilidad usando la fórmula de Bayes
p_u0_dado_l_y_t = numerador / denominador

print(f"\nLa probabilidad de que la dona provenga de la urna 0 dado que es de limón y en forma de toro es: {p_u0_dado_l_y_t:.4f}")
print("procedimiento similar al de los incisos anteriores")

