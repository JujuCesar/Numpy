import numpy as np

# Criando arrays
arr1 = np.arange(0,51,2)
arr2 = np.arange(100,50,-2)

# Concatenando arrays
arr3 = np.concatenate([arr1,arr2])

# Ordenando os pares
arr4 = np.sort(arr3)

print("Array concatenado: \n",arr3)
print("\n")
print("Array ordenado: \n",arr4)