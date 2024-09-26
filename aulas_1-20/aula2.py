'''
Função "Print()"
    - Usada para imprimir coisas na tela.
    - O argumento dado à função é que será mostrado.
    - Mais de argumento pode ser passado para a função.
        Eles devem ser dividos por vírgula " , ". 
'''
print("Hello, World!")

'''
O Argumento " sep='' "
    - Usado para definir o sinal que separa argumentos não-nomeados.
'''

print(12, 34, sep="-")
print(56, 78, sep=';')

'''
Quebras de linha Específicas: CRLF e LF
    - CRLF (Windows): Combinação de dois caracteres de controle:
        
        * O 'Carriage Return' (retorno de carro), representado pelo
        caractere "\r".

        * E o 'Line Feed' (avanço de linha), representado pelo
        caractere "\n".

        * Em conjunto, os dois caracteres indicam o início
        de uma nova linha de texto.

    - LF (Linux): O mesmo que 'Line Feed'.
'''

'''
O Argumento " end='' "
    - Usado para definir o comportamento da quebra de linha, inclusive exibindo
    símbolos pré-estabelecidos.
'''

print(12, 34, 1011, sep='/', end='#\n')