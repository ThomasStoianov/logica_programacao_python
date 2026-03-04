vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), (103,
"Teclado", 8, 150.0), (104, "Case", 3, 50.0)]

estoque_baixo = []

calculo_inventario = 0

lista_atualizada = []

for produto in vendas_brutas:
    if (produto[2] < 10):
        estoque_baixo.append(produto)
    
    calculo_inventario += produto[2] * produto[3]

    preco = produto[3]
    novo_preco = preco * 1.10

    nova_tupla = (produto[0], produto[1], produto[2], novo_preco)
    lista_atualizada.append(nova_tupla)

print(f"Produtos com estoque baixo {estoque_baixo}")
print(f"Total do valor do inventário: {calculo_inventario}")
print(f"Produtos com um aumento de 10%: {lista_atualizada}")