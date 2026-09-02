import os
# lista todos os arquivos do diretorio e retorna os nomes em uma lista
def run(**args):
    print("[*] No modulo dislister")
    files = os.listdir(".")
    return str(files)