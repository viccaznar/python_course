'''
Lista de listas e seus índices
'''

salas = [
    # 0      1
    ['Maria', 'Helea',],    # 0
    # 0
    ['Elaine',],            # 1
    # 0
    ['Luiz', 'Joao', 'Eduarda', ],  # 3
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][2][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)