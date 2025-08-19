import numpy as np

# Array só de 1's
arr1 = np.ones(8, dtype=int)

# Array de números aleatórios entre 0 e 9
arr2 = np.random.randint(0, 10, 8)

# Soma dos dois arrays
arr3 = arr1 + arr2
print("Array resultante:", arr3)

# Verificando soma dos elementos
soma = arr3.sum()
print("Soma dos elementos:", soma)

# Remodelando dependendo da soma
if soma >= 40:
    arr3 = arr3.reshape(4, 2)  # mais linhas do que colunas
else:
    arr3 = arr3.reshape(2, 4)  # mais colunas do que linhas

print("Array remodelado:\n", arr3)
