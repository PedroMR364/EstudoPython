# Pede um número e verifica se é Par ou Ímpar
numero = input("Digite um número: ")

# é necessário realizar a conversão de texto para número, pois a função input sempre retorna o valor para formato texto. Então, utilizamos a função int para converter a variável numero em valor númerico inteiro e assim realizar os cálculos necessários.
numero = int(numero)

if (numero % 2 == 0):
    print("O número digitdo é Par!")
else:
     print("O número digitado é Ímpar!")