# # Leia 2 valores de ponto flutuante de dupla precisão A e B, 
# # que correspondem a 2 notas de um aluno. A seguir, calcule a média 
# # do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 
# # (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0,
# # sempre com uma casa decimal.

# # Entrada
# # O arquivo de entrada contém 2 valores com uma casa decimal cada um.

# # Saída
# # Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, 
# # com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois 
# # da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, 
# # não esqueça de imprimir o fim de linha após o resultado,
# # caso contrário, você receberá "Presentation Error".

# A = float(input("Digita a nota da primeira avaliação: "));
# B = float(input("Digite a nota da segunda avaliação: "));

# media = (A * 3.5) + (B * 7.5) / 11; ## calcular peso: nota * peso / pela soma dos pesos (11) 


# print("MEDIA = {:.5F}".format(media))




# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno


# A = float(input("Digite a nota da primeira avaliação: "));
# B = float(input("Digite a nota da segunda avaliação: "));
# C = float(input("Digite a nota da segunda avaliação: "));

# # calcular media aluno. A tem peso = 2, B tem peso = 3, C = 5
# # nota * soma do peso / pela soma dos produtos
# media = (A * 2 + B * 3 + C * 5) / 10;

# print("MEDIA = {:.1F}".format(media));

# Leia quatro valores inteiros A, B, C e D. 
# A = int(input("Digite um número: "));
# B = int(input("Digite outro número: "));
# C = int(input("Digite outro número: "));
# D = int(input("Digite outro número: "));
 
# # A seguir, calcule e mostre a diferença do produto de A e B
# # pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

# diferenca = (A * B) - (C * D);

# print("DIFERENCA = {}".format(diferenca));


## SALÁRIO

# Escreva um programa que leia o número de um funcionário,
# seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.



