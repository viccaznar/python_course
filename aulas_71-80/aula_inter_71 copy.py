'''
Exercício com funções

1)Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.
'''
def multplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = multplicar(10, 2, 3, 4, 5)
print(multiplicacao)
print(10, 2, 3, 4, 5)

'''
2)Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é ímpar'


print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))