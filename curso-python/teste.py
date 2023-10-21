
# import glob
# import os 

# diretorio = input("Digite o nome da pasta que deseja buscar: ")
# extensao = input("Agora, digite o tipo de arquivo que deseja buscar: (exemplo: .txt, .jpg: ")

# meus_arquivos = glob.glob(os.path.join(diretorio, f"*{extensao}"))

# quantidade_arquivos = len(meus_arquivos)

# print(f"Contagem dos arquivos: '{extensao}': {quantidade_arquivos}")

# open("caminho", "r")

#r - leitura
# a - append/incrementar
# w - write / escrever
# x - criar arquivo
# r+ - Leitura + escrita

# arquivo = open("teste.txt", "r");

# # print(arquivo.readable()) #vai retornar verdade ou falso pra saber se esse arquivo pode ser lido
# print(arquivo.read());

# arquivo.close();


# import random;


# numero_aleatorio = random.random() * 100; #random retorna numero aleatorio entre 0 e 1 
# # que multiplicado por 100 retorna um numero entre 0 e 100, como uma porcentagem
# print(round((numero_aleatorio))); #round vai arredondar o numero decimal para um inteiro
# #se o numero for 54.754 o round() vai arredondar pra 55


def soma (a, b):
    return a + b

print(soma(2,3));
print(soma(10,5));



