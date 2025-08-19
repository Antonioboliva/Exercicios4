import numpy as np

# Fixando seed
np.random.seed(10)

# Criando matriz 4x4 com inteiros de 1 a 50
matriz = np.random.randint(1, 51, (4, 4))
print("Matriz:\n", matriz)

# a) Média de cada linha e coluna
media_linhas = matriz.mean(axis=1)
media_colunas = matriz.mean(axis=0)

print("\nMédia de cada linha:", media_linhas)
print("Média de cada coluna:", media_colunas)

# b) Maior valor das médias
maior_media_linhas = media_linhas.max()
maior_media_colunas = media_colunas.max()

print("\nMaior média das linhas:", maior_media_linhas)
print("Maior média das colunas:", maior_media_colunas)

# c) Contagem de aparições
valores, contagens = np.unique(matriz, return_counts=True)
print("\nQuantidade de aparições de cada número:")
for v, c in zip(valores, contagens):
    print(f"{v}: {c} vezes")

# Mostrar apenas os números que aparecem 2 vezes
print("\nNúmeros que aparecem 2 vezes:")
print(valores[contagens == 2])
