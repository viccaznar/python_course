'''
iterável -> str, range, etc (__iter__).
iterador -> quem sabe entregar um valor por vez.
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
'''

# for letra in texto
texto = 'Luiz' # iterável

'''
iteratador = iter(texto) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
'''
        
for letra in texto:
    print(letra)