import numpy as np

# Exportando o db

database = np.loadtxt('../space.csv', delimiter =';', dtype='str', encoding='utf-8')

# Varrendo o db e pegando missoes da SpaceX

spacex = database[:,1] == 'SpaceX'
filtro = database[spacex] # Aplica um filtro sob spacex pra nao dar erro

# Seleciando a coluna 'Cost'

custo = filtro[:,6].astype(float)

# Pegando maior valor

valor = np.max(custo)

# Pegando o maior valor

maior = np.max(valor)

# Pegando o numero da missao mais cara

num = np.argmax(custo)

# Mostrando valores

print(f"A Missão mais cara da SpaceX foi: {num}\n")
print(f"Com o custo total: {valor}")


