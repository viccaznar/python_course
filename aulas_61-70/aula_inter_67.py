'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

"""
Prints a greeting for each name in the list, first with "Bom dia" and then with "Boa noite".

This code demonstrates the use of closures, where the `criar_saudacao` function creates and returns a new function `saudar` that can be called with a name to generate a personalized greeting.
"""
for nome in ['Maria', 'Joane', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))