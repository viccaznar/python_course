'''
Faça uma lista de compras usando o tipo 'list'
    - O usuário deve ter a possibilidade de inserir, apagar e
    listar valores da sua lista.
    - Não permita que o programa quebre com erro
    de índices inexistentes na lista.
'''
import os

lista = []
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar' '[l]istar  ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor a ser adicioado: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao =='l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar')

        else:
            for i, item in enumerate(lista):
                print(i, item)
    else:
        print('Por favor, escolha [i] [a] ou [l]')
