def calcular_e(n):
    return (1 + 1/n) ** n

n = float(input("Digite um número: "))  # quanto maior, mais preciso
e_aproximado = calcular_e(n)

print(e_aproximado)