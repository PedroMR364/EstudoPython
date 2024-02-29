n1 = input("Digite a nota do Aluno: ")
n2 = input("Digite a segunda nota do Aluno: ")
n3 = input("Digite a terceira nota do Aluno: ")
n4 = input("Digite a quarta nota do Aluno: ")
rs = ( int(n1)+int(n2)+int(n3)+int(n4) ) / 4
#  Se o Aluno tiver uma média acima ou igaul a 7, então estará APROVADO!
#  Se a média for abaixo ou igual a 4, então estará REPROVADO!
#  Caso contrário estará em RECUPERAÇÃO!
print("A sua média é "+str(rs)+", então você está: ")

if( rs >= 7):
    print("Aprovado!")
elif( rs <= 4):
    print("Reprovado!")
else:
    print("Recuperação!")