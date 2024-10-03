'''
Iterando strings com While
'''

#           012345678910
nome =      'Luiz Otávio'   # Iteráveis
#           1110987654321

novo_nome = ''
indice = 0

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)