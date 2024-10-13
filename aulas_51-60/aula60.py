'''
Split e Join com str

    - slipt = divide uma string (list)
    - join une = uma sting
'''

frase = '   Ola só que  , coisa interessante'
lista_de_frase_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate (lista_de_frase_cruas):
    lista_frases.append(lista_de_frase_cruas[i].strip())

# print(lista_de_frase_cruas)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)