nome_cliente = input("Digite seu nome: ")
renda = float(input("Digite sua renda: "))
gasto_mensal = float(input("Digite seu gasto mensal: "))
coragem = int(input("Digite seu nível de coragem de 1 a 10. 1 para bem cauteloso e 10 para muito corajoso: "))
anos_investir = int(input("Digite quantos anos você pretende investir: "))

sobra_dinheiro = 0
reserva_seguranca = 0

if (gasto_mensal > renda):
    print("Emergência Financeira")
else:
    sobra_dinheiro = renda - gasto_mensal
    reserva_seguranca = gasto_mensal * 6

    print(f"Sobra mensal: R$ {sobra_dinheiro:.2f}")
    print(f"Reserva ideal (6x gasto): R$ {reserva_seguranca:.2f}")

    if (coragem < 4):
        print("Perfil Conservador: Tesouro Direto")
    elif (coragem >= 4 and coragem <= 7):
        print("Perfil Moderado: Fundos Imobiliários")
    else:
        print("Perfil Arrojado: Ações de Tecnologia")

    valor = 0
    taxa = 0.08

    for ano in range(1, anos_investir + 1):
        valor += sobra_dinheiro
        valor += valor * taxa
        print(f"Ano {ano}: R$ {valor:.2f}")

    print(f"{nome_cliente}, em {anos_investir} anos você pode ter R$ {valor:.2f}")