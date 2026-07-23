num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
mult = num1 * num2
divisao = num1 / num2

resultado = input("Qual operação você quer realizar? +, -, * ou /?: ")

if resultado == "+":
    print("Resultado: ", soma)
elif resultado == "-":
    print("Resultado: ", subtracao)
elif resultado == "*":
    print("Resultado: ", mult)
elif resultado == "/":
    print("Resultado: ", divisao)
else: print("Operação inválida!")