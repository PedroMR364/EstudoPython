def tabuada(numero=0):
    print("Digite um número para fazer a tabuada: ")
    arq = open("tabuada.txt","a")
    for i in range(1,11):
        arq.write(str(numero) + " x " + str(i) + " = " + str(numero*i)+"\n")
    arq.close()


n = input("Digite um número: ")
tabuada(int(n))