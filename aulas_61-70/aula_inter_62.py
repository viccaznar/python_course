'''
Argumentos nomeados e não nomeados em funções Python.
Argumentos nomeados tem o nome com o sinal de igual.
Argumrtos não nomeados recebe apenas o argumentos (valor)
'''

def soma(x, y, z):
    # definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3, )

soma(1, 2, 3)
print(1, 2, 3, sep='-')