saldo = 1000

deposito = float(input("Valor do depósito: "))
saldo += deposito

saque = float(input("Valor do saque: "))
saldo -= saque

saldo *= 1.05

print("Saldo final: ", saldo)