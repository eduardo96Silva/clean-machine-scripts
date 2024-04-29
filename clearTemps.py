import os
import shutil

# Função para fazer a limpeza das subpastas e arquivos que contém na pasta alvo
def limpar_pasta(pasta):
    for root, dirs, files in os.walk(pasta, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except (PermissionError, OSError): # Os except's -> vai para o proximo item do loop, caso haja algum arquivo sendo usado pelo sistema.
                continue
        for dir in dirs:
            try:
                shutil.rmtree(os.path.join(root, dir))
            except (PermissionError, OSError):
                continue

# Lista de caminhos para diretórios que contém arquivos temporários:
paths = [
    "C:/Windows/Temp",
    "C:/Users/eduar/AppData/Local/Temp" # Nesse caminho substitua o usuário para o seu usuário !
]

# Acionando a função para cada path da lista
for path in paths:
    limpar_pasta(path)