'''
Dicionários em Python (tipo 'dict'):
    - Dicionários são estruturas de dados do tipo
    par de 'chave' e 'valor'

Chaves:
    - Poder ser consideras como índices que vimos na lista
    e pode ser de tipos imutáveis.
    - Exemplos: str, int, float, bool, tuple
    - O valor pode ser de qualquer tipo, incluindo outro dicionário

Usamos as chaves  - {} - ou a classe dict para crias dicionário.

Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

pessoa = {
    'Nome': 'Luiz Otávio',
    'Sobrenome': 'Miranda',
    'Idade': 18,
    'Altura': 1.80,
    'Endereço': [
        {'Rua': 'Av. Paulista', 'número': 123}
        {'Rua': 'Av. Paulista', 'número':321}
}
pessoa = direct(nome='Luiz Otávo', sobrenome='Miranda')
'''
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.80,
    'endereço': [
        {'rua': 'Av. Paulista', 'número': 123},
        {'rua': 'Av. Paulista', 'número': 321},
    ]


}
# print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa['nome'])