import numpy as np

# Exportando o db

database = np.loadtxt('../paises.csv', delimiter =';', dtype='str', encoding='utf-8')

# Pegando países da Amerida Latina & Caribe
AL = database[:,1] == "LATIN AMER. & CARIB"
paisesL = database[AL]

# Pegando paises e suas rendas per capita
paises = paisesL[:,0]
percapta = paisesL[:,8]

# Convertendo para float
percapta = np.array([float(valor.strip()) if valor.strip() != "" else 0 for valor in percapta])# Verifica se não é vazio o dado no array

# Pando o maior GDP e Saida de dados
if percapta.size > 0:
    gdp = np.argmax(percapta)
    paisMAisRico = paises[gdp]
    maiorgdp = percapta[gdp]
    print(f"O pais mais rico da America do Sul & Caribe é {paisMAisRico} com um GDP per capta de ${maiorgdp:.2f}")



