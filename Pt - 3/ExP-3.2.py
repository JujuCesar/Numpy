import numpy as np

# Exportando o db

database = np.loadtxt('../space.csv', delimiter =';', dtype='str', encoding='utf-8')

# Varrendo o db e pegando os valores - Num;Company Name;Location;Datum;Detail;Status Rocket; Cost;Status Mission

valor = database[1:,6].astype(float) # pegando todas as linhas e apenas a coluna 6 ('Cost')

# Filtrando gastos

gastos = valor[valor > 0]

# Fazendo a média

media = np.mean(gastos)

# Mostrando a média de gastos das missões

print(f"Média de gastos das missões: ${media}")