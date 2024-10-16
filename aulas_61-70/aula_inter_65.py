'''
Exercícios com funções
    - Crie uma função que multipica todos os argumrntos
    não nomeados recebidos.
    Retorme o total para uma variável e mostre  valo da variavel,
'''

def multiplicar(*args):   
    total = 1

    for numeros in (args):
        total *= numeros
    return total

multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)

'''
Exercícios com funções
    - Crie uma função que fala se um par ou ímpar.
    - Rtorne se o número é par ou ímpar.
    '''

def par_impar(numero):
        multiplo_de_dois = numero % 2 == 0

        if multiplo_de_dois:
            return f'{numero} é Par'
        else:
            return f'{numero} é Ímpar'
        
outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)