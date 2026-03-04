# 3. Integração: Repetição WHILE + Condicionais + Atribuição:
# Exercício: Crie um programa que inicialize uma variável saldo = 500.0. Exiba um
# menu com as opções: (1) Depositar, (2) Sacar e (3) Sair.
# • Se escolher depositar, peça o valor e some ao saldo.
# • Se escolher sacar, verifique se há saldo suficiente; se sim, subtraia; se não,
# avise "Saldo Insuficiente".
# • O programa deve repetir (while) até que o usuário escolha a opção 3.

saldo = 500.0

print(saldo)

valor = 0

while True:
    mensagem = int(input("Menu: (1) Depositar, (2) Sacar, (3) Sair: "))

    if (mensagem == 1):
        valor = float(input("Digite o valor que será depositado: "))
        if (valor < 0):
            print("O valor não pode ser negativo")
        else:
            saldo = saldo + valor
            print(f"Seu saldo é de {saldo}R$")
    if (mensagem == 2):
        valor = float(input("Digite o valor que será sacado: "))
        if (valor > saldo):
            print("Saldo insuficiente")
        else:
            saldo = saldo - valor
            print(f"Seu saldo é de {saldo}R$")
    if (mensagem == 3):
        break