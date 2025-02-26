import numpy as np

# Criando matriz do campo minado
mtz = np.zeros([2,2])

# Somando o numero 1 em algum lugar da matriz kk
linha, coluna = np.random.randint(0, 2, 2) #Gera uma posição unica para o 1
mtz[linha, coluna] = 1 # Pega a posição gerada assima, acha ele na matriz e coloca como 1

# Exibindo matriz inicial
print(mtz)

# Iniciando o jogo
vida = 3
posicoes_descobertas = set() # Para verificar em loop

while vida != 0:
    try:
        x = int(input("Entre com um valor entre 0 e 1: "))
        y = int(input("Entre com um valor entre 0 e 1: "))

        # Se a posição ja tiver sido escolhida
        if (x,y) in posicoes_descobertas:
            print("Posição ja descoberta, insira outra")
            continue

        # Add a posição desconerta
        posicoes_descobertas.add((x,y))


        # Se acertar o 1 perde o jogo
        if mtz[x,y] == 1:
            print("Game Over! :( Try Again!")
            break
        vida -=1

        # Se todas as posições forem descobertas
        if len(posicoes_descobertas) == 3: # Foram descobretas todas as posições
            print("Congratulations! You beat the game! :)")
            break

    except ValueError:
        print("Entrada inválida!")