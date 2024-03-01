print("Este programa analisa se sua placa pode andar de acordo com a semana")
digito = input("Digite o ultimo digito da sua placa: ")

match digito:
    case '1' | '2':
        print("Sua placa não pode percorrer hoje, pois hoje é Segunda-Feira")
    case '3' | '4':
        print("Sua placa não pode percorrer hoje, pois hoje é Terça-Feira")
    case '5' | '6':
         print("Sua placa não pode percorrer hoje, pois hoje é Quarta-Feira")
    case '7' | '8':
         print("Sua placa não pode percorrer hoje, pois hoje é Quinta-Feira")
    case '9' | '0':
         print("Sua placa não pode percorrer hoje, pois é hoje Sexta-Feira")
    case _:
        print("Digito inválido, por favor, escreva outro!")