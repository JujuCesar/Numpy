import numpy as np

# Exportando o db

database = np.loadtxt('../space.csv', delimiter =';', dtype='str', encoding='utf-8')

# Contando o numenro de missoes bem sucedidas com uma mascara boolena para armazenar True's

success_n = np.char.find(database,'Success') >= 0

# Contando o numero total de missoes através da soma dos success_n

cont = np.sum(success_n)

# Mostrando numero total de missões bem sussedidas

print(f"Número de missões bem sussecidas: {cont}")