pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

resposta = 0

if (pergunta1 == "S" or pergunta1 == "sim" or pergunta1 == "Sim"):
    resposta += 1

if(pergunta2 == "S" or pergunta2 == "sim" or pergunta2 == "Sim"):
    resposta += 1

if(pergunta3 == "S" or pergunta3 == "sim" or pergunta3 == "Sim"):
    resposta += 1

if(pergunta4 == "S" or pergunta4 == "sim" or pergunta4 == "Sim"):
    resposta += 1   

if(pergunta5 == "S" or pergunta5 == "sim" or pergunta5 == "Sim"):
    resposta += 1    

if (resposta == 2):
    print("Suspeita")
elif (resposta == 3 or resposta == 4):
    print("Cúmplice")
elif (resposta == 5):
    print("Assassina")
else:
    print("Inocente")