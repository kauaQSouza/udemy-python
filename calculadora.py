def calculadora():
    print("CALCULADORA")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida.")

calculadora()
