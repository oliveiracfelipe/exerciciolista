nome = input("Digite um nome: ")
idade = int(input("Digite sua idade: "))

print("Nome: ", nome)
print("Idade: ", idade)
print("Quantidade de letras do nome: ", len(nome))
print("Nome em maiúsculo: ", nome.upper())
print("Nome em minúsculo: ", nome.lower())

if idade < 12:
    classificacao = "Criança"
elif idade < 18:
    classificacao = "Adolescente"
else: classificacao = "Adulto"

print("Classificação: ", classificacao)