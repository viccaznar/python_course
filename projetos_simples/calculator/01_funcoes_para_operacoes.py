'''
Estrutura de uma Função

    - def nome_da_funcao(parametro1, parametro2):
        # código que a função executa
        return resultado
'''

'''
def = Indica que você está definindo uma função.

nome_da_funcao = O nome que vocé dá para a função.

parâmetros = Variáveis que você passa para a função.

código: O bloco de código que a função executa quando chamada.

return: Retorna um valor da função. Sem um return, a função retornará 'None' por padrão.
'''

# Funções básicas para as funcionalidades da calculadora

def sum (x,y):
    return x + y

def subtraction (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y
