import numpy as np

# Exportando o db

database = np.loadtxt('../paises.csv', delimiter =';', dtype='str', encoding='utf-8')

# Pegando coluna de Regions
mtz = database[:,1]

# Contando quantos são da América do Norte
AN = np.char.find(mtz,"NORTHERN AMERICA") >= 0
total = np.sum(AN)

# Saida de dados
print(f"Qtd de paises da Amerida do Norte: {total}")