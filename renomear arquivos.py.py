import os

print("=======================================================\n")
print("ESTE SCRIPT TE AJUDA A RENOMEAR ARQUIVOS EM SEU COMPUTADOR\n(obs: até o momento só imagens. Haverá atualização em breve)\n\
      [ POR FAVOR, SIGA AS ESPECIFICAÇÕES]")
print("\n=======================================================\n")

folder = input("->  Caminho da pasta: ")
NOME = str(input("\n->  Nome padrão para renomear os arquivos:"))
EXTENSAO = str(input("\n->  Extensão do arquivo(sem ponto. Ex: png):"))

extensoes_imagens = ['png', 'jpg', 'jpeg']  

num = 0
for file in os.listdir(folder):
    nome_antigo = os.path.join(folder, file)
    extensao_arquivo = file.split('.')[-1].lower()  # Obtém a extensão do arquivo em letras minúsculas
    if extensao_arquivo in extensoes_imagens:
        num += 1  
        nome_novo = os.path.join(folder, f"{NOME}{num}.{EXTENSAO}")
        os.rename(nome_antigo, nome_novo)

print(os.listdir(folder))

print("\n=======================================================\n")
print("\nSeus arquivos foram renomeados. Olhe o diretório <", folder,"> para conferir \n\n")
print("\n=======================================================\n")