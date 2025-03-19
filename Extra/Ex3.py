import numpy as np

# Exportando o db

database = np.loadtxt('../paises.csv', delimiter =';', dtype='str', encoding='utf-8')

# Selecioando coluna Literacy
mtz = database[1:,9]

# Transformando em float os valores no array
mtz = np.array([float(valor) for valor in mtz if valor != ""]) # Verifica se não é vazio o dado no array

# Calcula a média
media = np.mean(mtz)

# Saida de dados
print(f"Taxa de alfabetização global: {media:.2f}%")