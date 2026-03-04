numero = float(input("Digite um número: "))

resultadoPositivo = ("Positivo" and (numero > 0)) or ("Negativo" and (numero < 0)) or ("Zero" and (numero == 0))

print(resultadoPositivo)