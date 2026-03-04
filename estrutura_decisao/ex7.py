compra = float(input("Digite o valor da sua compra: "))

if (compra > 100 and compra <= 200):
    desconto = compra * 0.10
    compra_final = compra - desconto
    print(f"Você obteve um desconto de 10%.Sua compra final é: {compra_final:.2f}")
elif (compra > 200 and compra <= 500):
    desconto = compra * 0.20
    compra_final = compra - desconto
    print(f"Você obteve um desconto de 20%.Sua compra final é: {compra_final:.2f}")
elif (compra > 500):
    desconto = compra * 0.30
    compra_final = compra - desconto
    print(f"Você obteve um desconto de 30%.Sua compra final é: {compra_final:.2f}")
else:
    print(f"Você não obteve desconto. Sua compra final é: {compra:.2f}")