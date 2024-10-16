'''
Higher Order Fuction
    - Funções de primeira classe
'''

def saudação (msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudação, 'Bom dia', 'Luiz'))

print(executa(saudação, 'Boa noite', 'Maria'))