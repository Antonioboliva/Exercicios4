import numpy as np
import random

# a) Criar array 2x2 só com zeros
campo = np.zeros((2, 2), dtype=int)

# b) Colocar o número 1 em posição aleatória
linha, coluna = random.randint(0,1), random.randint(0,1)
campo[linha, coluna] = 1

# c) Jogo
tentativas = 0
achou = False

while tentativas < 3 and not achou:
    print("\nDigite uma posição (linha e coluna de 0 a 1)")
    l = int(input("Linha (0 ou 1): "))
    c = int(input("Coluna (0 ou 1): "))

    if campo[l, c] == 1:
        print("💥 Game Over! :( Try Again!")
        achou = True
    else:
        print("✅ Safe spot!")
    tentativas += 1

if not achou:
    print("🎉 Congratulations! You beat the game! :)")
