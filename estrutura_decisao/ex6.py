nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print(f"Você foi aprovado!")
else:
    print("Você foi reprovado!")