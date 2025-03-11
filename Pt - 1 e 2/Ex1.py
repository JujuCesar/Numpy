import numpy as np
from numpy.ma.core import reshape

# Criando arrays
arr1 = np.ones([1,8])
arr2 = np.random.randint(0,9,8)

# Somando as arrays
arr3 = arr1 + arr2

soma = arr3.sum()

# Calculando dados
if soma >= 40:
    arr3 = arr3.reshape(4,2) # Mais linhas que colunas
else:
    arr3 = arr3.reshape(2,4) # Mais colunas que linhas

# Saída de dados
print(arr3)

