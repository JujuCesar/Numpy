import numpy as np

# Criando matriz de tamanho aleatorio
linhas = np.random.randint(2,6) # N de linas entre dois e seis
colunas = np.random.randint(2,6) # N de colunas entre dois e seis
matriz = np.random.randint(2,6,(linhas,colunas)) # Preenchendo a matriz com numeros aleatorios e passando as linhas e colunas

# Pegando o numero de linhas e colunas
nL, nC = matriz.shape

# Calculando o numero total de linas e colunas
total = nL * nC

# Verificando se o n de elemtnos é par ou impar
if total % 2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"

# Saída de dados
print("Matriz: ")
print(matriz)
print(f"\nLinas: {nL}, Colunas: {nC}\n")
print(f"Numero total: {total}, {resultado}")
print(f"\nA matriz podera ser reescrita com um numero ", resultado)

