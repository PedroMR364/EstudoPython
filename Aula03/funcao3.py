def criaArquivo(nome="",ext="", cont="") -> str:
    """A função criaArquivo recebe o nome do arquivo a extensão e por fim algo para inserir no arquivo, e criar este arquivo no diretório local"""
    f = open(nome+"."+ext,"a")
    f.write(cont)
    f.close
    return "Arquivo criado com êxito!"

print(criaArquivo("janela","bat","texto;mensagem;ola"))