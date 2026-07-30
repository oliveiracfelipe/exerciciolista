saldo = 1000

nome = input("Digite seu nome: ")
deposito = int(input("Valor do depósito: "))
saque = int(input("Valor do saque: "))
saldo += deposito

if saque > saldo:
    print("Saldo insuficiente!")
else: 
    saldo -= saque

print("==== RESUMO ====")
print("Nome: ", nome.upper())
print("Quantidade de letras: ", len(nome))
print(f"Saldo final: R$ {saldo:.2f}")