'''
Exiba o índice das listas
    - 0: Maria
    - 1: Helena
    - 2: Luiz
'''

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))