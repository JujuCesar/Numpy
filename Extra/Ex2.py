import numpy as np

# Exportando o db

database = np.loadtxt('../paises.csv', delimiter =';', dtype='str', encoding='utf-8')

# Pegando a colnuna das regioes e pulando o cabeçalho
mtz = database[1:,1]

# Contando o numero de regioes
regiUnica, cont = np.unique(mtz, return_counts=True) # Atribui os valores aos regiUnica e cont

# Saida de dados
print(f"Numero de Regiões diferentes: {cont}")
print("")
print(f"Regiões:")
for regiao in regiUnica:
    print(f"- {regiao}")

