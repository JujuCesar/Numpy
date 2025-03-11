import numpy as np

# Exportando o db

database = np.loadtxt('../space.csv', delimiter =';', dtype='str', encoding='utf-8')

# Varrendo o db e pegando quantas missoes foram feitas pelos Yankees

yankee = np.char.find(database,'USA') >= 0

# Contanto o numero de vezes que EUA são retornados como TRUE

cont = np.sum(yankee)

# Mostrando o numero de missoes feitas pelos Yankees

print(f"Missões realizadas pelos EUA: {cont}")



