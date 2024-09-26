'''
Tipos 'int' e 'float':
    
    - int = numero inteiro.
        - o int pode representar qualquer numero que nao possua casa decimal.
        - o int sem sinal de menos é considerado positivo.

    - float = numero com casa decimal ou ponto flutante.
        - o float representa qualquer numero, positivo ou negativo, com ponto flutuante.
        - o float sem sinal de menos é considerado positivo.

NOTA: Casa decimal deve ser separada por ponto ( . ).   
'''

print(11) # int
print(-11) # int

print(1.1, 10.11) # float

'''
Função Type()
    - mostra o tipo que o Python inferiu ao valor.
'''

print(type('Otavio'))
print(type(1))
print(type(0))
print(type(-1))
print(type(1.1), type(-1.1), type(0.0))