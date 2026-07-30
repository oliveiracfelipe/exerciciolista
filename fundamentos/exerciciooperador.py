nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 12:
    classificacao = "Criança"
elif idade < 18:
    classificacao = "Adolescente"
else:
    classificacao = "Adulto"

print("Olá,", nome + "!")
print("Você possui", idade, "anos.")
print("Classificação: ", classificacao)