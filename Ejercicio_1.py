# Teoria de Probabiliades - Laboratorio 2
# Autor: Gerardo Andre Fernandez Cruz - 23763
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
print("\nCálculo paso a paso:")
for i in range(3):
    prob_urna = pu[i] * pl_u[i] * pt_lyu[i]
    print(f"Urna {i}: P(U={i}) * P(L|U={i}) * P(T|L,U={i}) = {pu[i]:.4f} * {pl_u[i]:.4f} * {pt_lyu[i]:.4f} = {prob_urna:.4f}")