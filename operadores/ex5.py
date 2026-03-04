numero = int(input("Digite um número: "))

resto = numero % 2

resultado = ("Par" * (1 - resto)) + ("Ímpar" * resto)

print(resultado)