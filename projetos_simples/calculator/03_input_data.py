def collect_data():
    # Função está comentada, pois não está definida neste arquivo.
    # display_menu()
    
    choice = input("Enter your choice [1][2][3][4]: ")

    num1 = input("Enter the first number: ")
    # Conversão de tipo em variável separada.
    float_num1 = float(num1)

    num2 = input("Enter the second number: ")
    # Conversão de tipo em variável separada.
    float_num2 = float(num2)

    return f'A opção {choice=} foi escolhida. Os números digitados são {num1=} e {num2=}.'