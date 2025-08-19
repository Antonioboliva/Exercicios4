import numpy as np

# Array de pares de 0 até 50
arr1 = np.arange(0, 52, 2)

# Array de pares de 100 até 50 (descendo)
arr2 = np.arange(100, 49, -2)

# Concatenando
arr_total = np.concatenate((arr1, arr2))

# Ordenando
arr_total = np.sort(arr_total)

print("Array concatenado e ordenado:\n", arr_total)
