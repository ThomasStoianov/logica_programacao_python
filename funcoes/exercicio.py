nome_filial = input("Digite o nome da sua filial: ")

valores_vendas = []

while True:
    valor_venda = float(input("Digite o valor da venda: "))

    if (valor_venda == 0):
        break
    else:
        valores_vendas.append(valor_venda)
        print(valores_vendas)

def limpar_vendas(valores_vendas):
    nova_lista = []

    for valor in valores_vendas:
        if (valor > 0 and valor < 10000):
            nova_lista.append(valor)

    return nova_lista

nova_lista = limpar_vendas(valores_vendas)

def analisar_dados(nova_lista):
    soma_lista = sum(nova_lista)
    quantidade_items = len(nova_lista)

    faturamento = soma_lista
    media = soma_lista / quantidade_items

    return (faturamento, media)

faturamento, media = analisar_dados(nova_lista)

print(f"Seu faturamento foi de {faturamento:.2f}")
print(f"Sua média das vendas foi {media:.2f}")

def definir_status(media):
    if media > 5000:
        return "Alta Performance"
    elif 2000 <= media <= 5000:
        return "Performance Estável"
    else:
        return "Performance Crítica"

status_performance = definir_status(media)

print("\n====== RELATÓRIO DA FILIAL ======")
print(f"Filial: {nome_filial}")
print(f"Status de Performance: {status_performance}")
print(f"Faturamento Total: R$ {faturamento:.2f}")
print(f"Média das Vendas: R$ {media:.2f}")

print("\nVendas Válidas:")

contador = 1

for valor in nova_lista:
    print(f"{contador} - R$ {valor:.2f}")
    contador +=1