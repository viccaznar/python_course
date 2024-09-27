'''
Operadores Lógicos

and [e]:
    - Todas as condições precisam ser verdadeiras.
    Se qualquer valor for considerado falso,
    a expressão inteira será avaliada como FALSA.

or [ou]:
    - Sendo uma das condições verdadeira,
    a expressão será avaliada como VERDADEIRA.

- not [não]
    - Comparação que busca negar uma condição.
    Sendo a negativa da condição verdadeira,
    a expressão será avaliada como VERDADEIRA.
'''

'''
Valores consideradados falsos (Falsy values)
    - 0
    - 0.0
    - ''
    - False
'''

'''
Tipo NONE
    - Usado para representar um não valor.
'''

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de Curto Circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)