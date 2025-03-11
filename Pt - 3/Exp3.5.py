import numpy as np

# Exportando o db

database = np.loadtxt('../space.csv', delimiter =';', dtype='str', encoding='utf-8')

# Pegando a aprtir do cabeçalho e a coluna do 'Name'

empresas = database[1:,1]

# Varendo o db e pegando cada unico nome e a contagem de vezes que ela fez missoes
nomes_empresas, contagem = np.unique(empresas, return_counts=True) # Joga o numero contado para contagem com return_conts

# Mostrando as infos de cada empresa com for
for nomes, qtd in zip(nomes_empresas, contagem):
    print(f"A empresa {nomes} realizou {qtd} missões.") # Zip usado para linkar dois iteráveis (nomes_empresas - contagem)