# 2. Integração: Repetição FOR + Operadores de Associação:
# Exercício: Peça para o usuário digitar uma frase ou nome completo. Utilizando um
# laço for, percorra cada caractere da string e verifique se ele é uma vogal (utilizando
# o operador in "aeiouAEIOU"). Ao final, exiba o total de vogais encontradas.

frase = input("Digite uma frase ou um nome completo: ")

vogais = "aeiouAEIOU"

contador = 0

for vogal in frase:
    if vogal in vogais:
        contador += 1
print(f"A palavra tem {contador} vogais")