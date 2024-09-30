'''
Exercício 1
    - Faça um programa que peça ao usuário para digitar um número inteiro,
    - Informe se este número é par ou ímpar.
        Caso o usuário não digite um número inteiro, informe que não é um
        número inteiro.
'''
entrada = input('Digite um número: ')

try:
    entrada_int = int(entrada)
    entrada_par = entrada_int % 2 == 0
    par_ou_impar_texto = 'ímpar'

    if entrada_par is True:
        par_ou_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_ou_impar_texto}')

except:
    print('Você não digitou um número inteiro')


# Segunda Solução
'''
if entrada.isdigit():
    entrada_int = int(entrada)
    entrada_par = entrada_int % 2 == 0
    par_ou_impar_texto = 'ímpar'

    if entrada_par is True:
        par_ou_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_ou_impar_texto}')

else:
    print('Você não digitou um número inteiro')
'''