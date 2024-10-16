'''
Dicionários em Python (tipo dict)

Dicionarios são estruturas de dados do tipo par de "chave" e "valor".
    - Chaves podem ser consideradas como o "índice" que vimos na lista
     e podem ser de tipos imutáveis como: 
        - str, int, float, bool, tuple, etc.

- O valor pode ser de qualquer tipo, incluindo outro dicionário.
- Usamos as chaves - {} - ou a classe dict para criar dicionários.
- Imutáveis:
    - str, int, float, bool, tuple
- Mutáveis:
    - dict, list

'''
# printdict(dict(nme = 'Luiz Otávio', sobrenome = 'Miranda)
pessoa = {
        'nome': 'Luiz Otávio',
        'sobrenome': 'Miranda',
        'idade': 18,
        'altura': 1.80,
        'endereços': [
            {'rua': 'tal tal', 'número': 123},
            {'rua': 'outra rua', 'número': 321},
        ]
    }

# print(pessoa), type(pessoa))
    
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

