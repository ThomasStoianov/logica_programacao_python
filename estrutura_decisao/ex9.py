salarioAtual = float(input("Digite o seu salário mensal para o reajuste: "))

if (salarioAtual < 280):
    aumento = salarioAtual * 0.20
    salarioNovo = salarioAtual + aumento
    print(f"Seu salário antes era: {salarioAtual}, o percentual aplicado foi de 20%, o valor do aumento foi de {aumento} e seu novo salário é de {salarioNovo}")
elif (salarioAtual >= 280 and salarioAtual < 700):
    aumento = salarioAtual * 0.15
    salarioNovo = salarioAtual + aumento
    print(f"Seu salário antes era: {salarioAtual}, o percentual aplicado foi de 15%, o valor do aumento foi de {aumento} e seu novo salário é de {salarioNovo}")
elif (salarioAtual >= 780 and salarioAtual < 1500):
    aumento = salarioAtual * 0.10
    salarioNovo = salarioAtual + aumento
    print(f"Seu salário antes era: {salarioAtual}, o percentual aplicado foi de 10%, o valor do aumento foi de {aumento} e seu novo salário é de {salarioNovo}")
elif(salarioAtual >= 1500):
    aumento = salarioAtual * 0.05
    salarioNovo = salarioAtual + aumento
    print(f"Seu salário antes era: {salarioAtual}, o percentual aplicado foi de 5%, o valor do aumento foi de {aumento} e seu novo salário é de {salarioNovo}")
else:
    print(f"Você não tem direito a receber um reajuste salarial, seu salário é de {salarioAtual}")