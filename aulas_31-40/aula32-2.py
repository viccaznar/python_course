'''
Exercício 2
    - Faça um programa que pergunte a hora ao usuário e,
    baseando-se no horário descrito, exibe a saudação apropriada.
        Exemplo:
            - Bom dia (0-11)
            - Boa tarde (12-17)
            - Boa noite (18-23)
'''

entrada_hora = input('Digite uma hora qualquer (0-11|12-17|18-23) em números inteiros: ')

try:
    entrada_hora_int = int(entrada_hora)

    if entrada_hora_int >=0 and entrada_hora_int <=11:
        print('Bom dia!')
    elif entrada_hora_int >=12 and entrada_hora_int<=17:
        print('Boa tarde!')
    elif entrada_hora_int >=18 and entrada_hora_int<=23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')
except:
    print('Você não digitou um número inteiro.')