'''
Exercício 2
    - Faça um programa que peça o primeiro nome do usuário.
        Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto."
        Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal."
        Se o nome tiver 6 letras ou mais, escreva "Seu nome é longo."
'''

entrada_nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(entrada_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'Seu nome é curto. Ele possui {tamanho_nome} letras')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'Seu nome é normal. Ele possui {tamanho_nome} letras')
    else:
        print(f'Seu nome é longo. Ele possui {tamanho_nome}')
else:
        print('Por favor, digite ao menos uma letra.')