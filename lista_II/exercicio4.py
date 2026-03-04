# 4. Integração: Identidade + Coleções Simples:
# Exercício: Na Ciência de Dados, entender se estamos copiando um dado ou
# apenas criando uma referência é vital.
# Crie uma lista dados_originais = [10, 20, 30].
# 1. Crie dados_referencia = dados_originais.
# 2. Crie dados_copia = [10, 20, 30].

# Use o operador is para mostrar ao aluno que dados_referencia é o mesmo
# objeto que o original, mas dados_copia não é, apesar de terem valores
# idênticos.

dados_originais = [10, 20, 30]
dados_referencia = dados_originais
dados_copia = [10, 20, 30]

print("dados referência é o mesmo que dados originais", dados_referencia is dados_originais)

print("dados copia não é dados referência", dados_copia is not dados_referencia)