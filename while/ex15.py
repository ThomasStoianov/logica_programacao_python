salario = float(input("Digite o seu salário: "))
ano = int(input("Digite o ano. Ex: 2020:"))
taxa = 0.015

while ano < 2026:
    aumento = salario * taxa
    salario += aumento
    taxa *= 2
    ano += 1
    print(f"{salario:.2f}")