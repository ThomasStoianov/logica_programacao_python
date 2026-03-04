print("Bem vindo ao planeta Alphara-7")
print("Saindo da nave")

dados_coletados = []

def obstaculo():
        while True: 
            encontrou_obstaculo = input("Obstaculo encontrado? S/N: ")

            if (encontrou_obstaculo == "s" or encontrou_obstaculo == "S"):
                return superar_obstaculo()
            elif (encontrou_obstaculo == "n" or encontrou_obstaculo == "N"):
                return condicao_cientifica()
            else:
                print("Digite apenas S ou N")

def superar_obstaculo():
        while True: 
            modo_obstaculo = input("Voces irao escalar ou contornar a montanha?: ")

            if (modo_obstaculo == "escalar"):
                return escalada_montanha()
            elif (modo_obstaculo == "contornar"):
                return contornar_montanha()
            else:
                print("Digite apenas 'escalar' ou 'contornar'")

def escalada_montanha():
        while True:  
            desempenho = input("Tiveram sucesso ao escalar a montanha? S/N: ")

            if (desempenho == "s" or desempenho == "S"):
                return condicao_cientifica()
            elif (desempenho == "n" or desempenho == "N"):
                return superar_obstaculo()
            else:
                print("Digite apenas S ou N")

def contornar_montanha():
        while True:  
            desempenho = input("Tiveram sucesso ao contornar a montanha? S/N: ")

            if (desempenho == "s" or desempenho == "S"):
                return condicao_cientifica()
            elif (desempenho == "n" or desempenho == "N"):
                return superar_obstaculo()
            else:
                print("Digite apenas S ou N")

def condicao_cientifica():
     while True:
          area_rica = input("Encontraram uma area rica em minerais ou sinais de vida? S/N: ")

          if (area_rica == "s" or area_rica == "S"):
               return coleta_dados()
          elif (area_rica == "n" or area_rica == "N"):
               return obstaculo()
          else:
               print("Digite apenas sim ou nao")

def coleta_dados():
     while True:
                    
          while True:
               dados = input("Digite o que voces encontraram, digite 0 para parar: ")

               if (dados == "0"):
                    break
               
               dados_coletados.append(dados)

          for dado in dados_coletados:
               print(dado)

          prosseguir = input("Digite 'R' para retornar a nave ou 'C' para continuar a missao: ")

          if (prosseguir == "C" or prosseguir == "c"):
               return obstaculo()
          elif (prosseguir == "R" or prosseguir == "r"):
               return fim_exploracao()
          else:
               print("Digite apenas C ou R")

def fim_exploracao():
    print("Esse é o fim da exploração, obrigado a todos por jogarem!")
    return

obstaculo()