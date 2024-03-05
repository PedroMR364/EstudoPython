nome_arquivo = input("Digite o nome do arquivo: ")
extensão_arquivo = input("Digite a extensão do arquivo: ")
conteudo = input("Digite o conteuúdo do arquivo: ")

arq = open(nome_arquivo+"."+extensão_arquivo,"a")
arq.write(conteudo)
arq.close()