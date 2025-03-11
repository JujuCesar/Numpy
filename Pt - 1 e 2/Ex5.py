import numpy as np

# Criando matrz
np.random.seed(10)
arr = np.random.randint(1,50,(4,4))

# Saída de dados
# A)
print("Matriz:")
print(arr)

print("Média:")
mediaL = np.mean(arr,axis = 1) # Calculando linha
mediaC = np.mean(arr, axis= 0) # Calculando coluna

print(f"Linha: ", mediaL)
print(f"Coluna: ", mediaC)

print("")

# B)
print("Maior valor da média:")
maiorLinha = np.max(mediaL)
maiorColuna = np.max(mediaC)

print("Maior linha: ",maiorLinha)
print("Maior coluna: ",maiorColuna)

print("")

# C)
print("Aparições de numeros: ")
valores, contagens = np.unique(arr, return_counts=True)
freqV = dict(zip(valores, contagens)) # Zip transforma duas matriz em uma, e dict transorma a matriz juntada em um dicionário

print("Frequencia de cada numero da matriz: ")
for num, freq in freqV.items(): # Verifica cada item(chave valor) da matriz
    print(f"Número {num}:{freq} vezes.")

numeros2X = [numero for numero, freq in freqV.items() if freq == 2]

print("\nNúmeros que aparecem exatamente 2 vezes:", numeros2X)

