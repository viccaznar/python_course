# Calculadora com While

while True:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')
    operador = input('Digite o operador [+][-][*][/]: ')

    primeiro_numero_float = 0
    segundo_numero_float = 0

    numeros_validos = None
    operadores_validos = '+-/*'

    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador not in operadores_validos:
        print('Operador inválido')
        continue
    
    print('Realizando os cálculos. Confira o resultado')
    if operador == '+':
        print(f'{primeiro_numero_float} + {segundo_numero_float} =', primeiro_numero_float + segundo_numero_float)
    elif operador == '-':
        print(f'{primeiro_numero_float} - {segundo_numero_float} =', primeiro_numero_float - segundo_numero_float)
    elif operador == '*':
        print(f'{primeiro_numero_float} * {segundo_numero_float} =', primeiro_numero_float * segundo_numero_float)
    elif operador == '/':
        print(f'{primeiro_numero_float} / {segundo_numero_float} =', primeiro_numero_float / segundo_numero_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [S]im ou [N]ão ').lower().startswith('s')
    print(sair)

    if sair == True:
        break