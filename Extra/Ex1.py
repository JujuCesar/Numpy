import numpy as np

# Exportando o db

database = np.loadtxt('../paises.csv', delimiter =';', dtype='str', encoding='utf-8')

# Exibindo apenas as colunas Country, Region, Pop e Area
mtz = database = database[:,[0,1,2,3]]

# Saída de dados
print("Paíese: \n")
print(mtz)