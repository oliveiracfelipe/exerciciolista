opcao = -1

while opcao != 0:

    print("===== CALCULADORA =====")

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        totalsoma = num1 + num2
        print("Resultado soma: ", totalsoma)

    elif opcao == 2:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        totalsubtracao = num1 - num2
        print("Resultado subtração: ", totalsubtracao)

    elif opcao == 3:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        totalmultiplicacao = num1 * num2
        print("Resultado mutliplicação: ", totalmultiplicacao)

    elif opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            totaldivisao = num1 / num2
            print("Resultado divisão: ", totaldivisao)
    elif opcao == 0:
        print("Você saiu da calculadora!")
    else:
        print("Opção inválida!")