import numpy as np

# Numpy Array Unidimensional
#arr = np.array([1, 2, 3])

# Numpy Array Bidimensional
#mtzT = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

#print(arr)
#print(mtzT)

 # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Criando de maneira mais facil
# Estruturando rapidamente uma matriz de 1's
#mtz1 = np.ones([5,5])
#print(mtz1)

# Estruturando rapidamente uma matriz de 0's
#mtz0 = np.zeros([5,5])
#print(mtz0)


# arange - Cria originalmente um array unidimensional normal
#mtz = np.arange(10)
#print(mtz)

# Criando uma array de 10 até 30 indo de 2 em 2
#arr = np.arange(10, 30, 2)
#print(arr)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Operações com Numpy arrays
#arr1 = np.array([1,2,3,4])
#arr2 = np.array([5,6,7,8])

#print(arr1.min(), arr1.max())
#print(arr1.argmin(), arr1.argmax())

#print(arr1.mean(), arr1.sum())

# Operações entre dois ou mais arrays
# Somando os valores com array
#arr3 = arr1 + arr2
#print(arr3)

# Concatenando as arrays
#arr4 = np.concatenate([arr1,arr2])
#print(arr4)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Reshape de numpy arrays

#mtz = np.arange(9).reshape(3,3)
#print(mtz)

#print(mtz.size)
#print(mtz.shape)
#print(mtz.ndim)

#  Operações nas linhas e colunas da matriz

#print(mtz.sum(axis=0)) # Somando colunas
#print(mtz.sum(axis=1)) # Somando linhas

#print(mtz.sum(axis=0)[0]) # Somando a primeira coluna apenas
#print(mtz.sum(axis=1)[0]) # Somando a primeira linha apenas

# Broadcasting

#print(mtz/2)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

# Elementos aleatorios e unicos

# Gerando numeros aleatorios
np.random.seed(10) # Ao adicionar uma semente, voce gera os mesmos numeros aleatorios
arr = np.random.randint(20,50,10) # Uni dimensional
print(arr)

arr2 = np.random.randint(20,50,[2,2]) #  Bi dimensional
print(arr2)

# Extraindo elementos unicos com unique
arr3 = np.random.randint(20,50,[5,5])
print(np.unique(arr3, return_counts=True))

