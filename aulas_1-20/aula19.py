primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)


if int_primeiro_valor > int_segundo_valor:
    print(f'O {int_primeiro_valor=} é maior que o {int_segundo_valor=}')
else:
    print(f'O {int_segundo_valor=} é maior que o {int_primeiro_valor=}')
