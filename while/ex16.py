preco_produto = float(input("Digite o preço do produto, Digite 0 para finalizar: "))
soma = 0
quantidade = 0

while preco_produto != 0:
    while preco_produto < 0:
        print("O preço do produto não pode ser negativo!")
        preco_produto = float(input("Digite o preço do produto, Digite 0 para finalizar: "))

    soma += preco_produto
    quantidade +=1
    preco_produto = float(input("Digite o preço do produto, Digite 0 para finalizar: "))

media = soma / quantidade

print(f"Soma dos produtos: {soma}")
print(f"Quantidade de produtos: {quantidade}")
print(f"Média do preço por produto: {media:.2f}")