'''
Listas em Python

Tipo 'list' = Mutável
    - Suporta vários valores de qualquer tipo.
    - Conhecimentos reutilizáveis - índices e fatiamentos
    - Métodos úteis:
        - append
        - insert
        - pop
        - del
        - clear
        - extend
        - +
'''

#        +01234   
string = 'ABCDE'    # 5 caracteres (len)
#        -54321

# print(bool([]))   # falsy   
# print(lista, type(lista))

lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))