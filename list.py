frutas = ["Maçã", "Pêra", "Laranja", "Uva", "Banana"]

frutas.append("Goiaba")

frutas.remove("Maçã")

for fruta in frutas:
    print(fruta) # dentro do for

print("Sobraram o total de",len(frutas), "Frutas") # fora do for