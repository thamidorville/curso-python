
##1) criar programa para buscar arquivo pelo nome informado pelo usuário

import os

direto = input("Informe o diretório que deseja pesquisar: ")

## Use a função os.listdir() para acessar os arquivos no diretório.

arquivos = os.listdir(direto)

#Armazene o nome dos arquivos em uma variável vetor, onde cada elemento do vetor será um nome de arquivo no diretório informado pelo usuário.

variavel_vetor = []

for arquivo in arquivos:
  variavel_vetor.append(arquivo)

print(f'{variavel_vetor[1]}')
