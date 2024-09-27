'''
Operador Lógico "NOT"

Usado para inverter expressões
    
    - not True = False
    - not False = True
'''

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
elif not senha:
    print('Você não digitou nada')
else:
    print('Senha Incorreta')

print(not True)     # False
print(not False)    # True