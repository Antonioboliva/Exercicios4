import numpy as np

# Criando uma matriz qualquer (ex: 3x4)
matriz = np.random.randint(1, 10, (3, 4))
print("Matriz:\n", matriz)

# Número de linhas e colunas
linhas, colunas = matriz.shape
print("Linhas:", linhas, " Colunas:", colunas)

# Multiplicando
total_elementos = linhas * colunas
print("Total de elementos:", total_elementos)

# Verificando se é par ou ímpar
if total_elementos % 2 == 0:
    print("O vetor unidimensional teria um número PAR de elementos.")
else:
    print("O vetor unidimensional teria um número ÍMPAR de elementos.")
