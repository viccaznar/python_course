'''
Interpolação Básica de Strings

    - s         = string

    - d e i     = int

    - f         = float

    - x e X     = Hexadecimal (ABCDEF123456789)
'''

'''
(Caractere)(><^)(Quantidade)

    > : Esquerda
    < : Direita
    ^ : Centro
    = : Força o número a aparecer antes do zeros

'''

'''
Sinal - + ou -

    Exemplo: 0>-100,1.f
'''

'''
Conversion flags = !r, !s, !a
'''

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746: 0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')