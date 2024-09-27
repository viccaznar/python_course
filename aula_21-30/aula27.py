'''
Exercício

    - Peça ao usuário para digitar seu nome.
    - Peça ao usuário para digitar sua idade.

    Se nome e idade forem digitados:

        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome_invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {primeira_letra}
            A última letra do seu nome é {ultima_letra}

    Se nada for digitado em nome ou idade:

        Exiba:
            "Desculpe, você deixou campos vazios."
'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
int_idade = int(idade)

print(f'Seu nome é {nome}')