'''
Type Convertion.

Conhecido também como:
    - Coersão de tipos
    - Converção de tipos
    - Typecasting
    - Coersion

É o ato de converter um tipo para outro.
'''

print(1 + 1) # Soma
print('a' + 'b') # Concatenação

# Nas duas funções acima, o mesmo sinal de + possui finalidades diferentes.
# A isso é dado o nome de Polimorfismo.
# Quando um mesmo signo possui finalidades distintas.

'''
Tipo imutáveis e primitivos:
    - str, int, float, bool.
'''

print('1', type('1'))
print(int('1'), type(int('1')))

print(int('1') + 1)
print(float('1') + 1)
print(type(float('1') + 1))

print(bool(''))
print(bool(' '))

print(str(11) + 'b')