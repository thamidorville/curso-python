# EXERCÍCIOS :  VETORES  E ARQUIVOS (AULA 06)

# 1) Crie uma versão do código de exemplo:10) Salvando dados do vetor em arquivo.
# Veja o conteudo do arquivo com o comando:
# more ./meu_dir/arq_1.txt, para um SISTEMA DE CONTROLE DE PRODUTOS que receba os dados
# preenchendo os vetores
# e ainda salve as informações em arquivo conforme apresentado na aula 05.

# O arquivo deve ser aberto em modo leitura ('r') ou escrita ('a'), de acordo com a operação.

# Pesquise no Google sobre "manipulação de arquivos em Python".

# Uma opção para ler os dados é utilizar a função readlines.

# Observação:

# Salve em uma linha o nome do produto e o preço. Exemplo:

# PROD1 5.99

# PROD2 2.50

# PROD3 19.80

# Toda vez que o programa for executado, os dados no arquivo devem ser lidos e copiados para o vetor.
# minha resolução:
# import os;

# lista de produtos e preço na mesma linha:
# lista_produtos = [
#     ("Blusa_amarela", 259.99),
#     ("Saia_marrom", 300.50),
#     ("Colar de Prata", 129.90)
# ];

# print("Lista de Produtos: {}" .format(lista_produtos));

# for produto, preco in lista_produtos:
#     print(f"{produto}: R$ {preco:.2f}");


livros = []
precos = []


def salvar_produto_na_lista_de_arquivos():
    # tudo que ta nesse aqrquio txt vai ser guardado na variavel lista_livros
    with open("lista_livros.txt", "w") as lista_livros:
        for i in range(len(livros)):  # o contador vai iterar pelo vetor inteiro
            # a funcao write vai coklovar esses valores
            lista_livros.write(f'{livros[i]}, {precos[i]:.2f}\n')
            # escrever esses valores e colocar na posição o livro e  o preço do lado


def exibir_arquivo_produtos():
    try:
        with open("lista_livros.txt", "r") as lista_livros:
            # lê todos os livros contidos na lista_livros e guarda na variável linhas
            linhas = lista_livros.readlines()
            for linha in linhas:  # para cada linha em linhas
                # strip p remorever espaço indesejado e split pra separar por vírgula
                livro, preco = linha.strip().split(', ')
                # livros.append(livro)
                # precos.append(float(preco))
                print(f'Livro: {livro}, Preço: {preco}');

                print("Dados lidos do arquivo: ");
                print(livros)
                print(precos)

    except FileNotFoundError:
        pass


while True:
    print("Opções: ")
    print("(1) Para visualizar a listagem dos livros da loja: ")
    print("(2) Para adicionar um livro na listagem: ")
    print("(3)Sair")

    opcao = input("Digite o número correspondente à opção desejada:  ")

    if opcao == "1":
        exibir_arquivo_produtos()  # chamando a função para que ela seja executada
        print("Listagem de livros da loja: ")
        for i in range(len(livros)):
            print(f'Livro: {livros[i]}, Preço: {precos[i]:.2f}')
    elif opcao == "2":
        livro = input("Digite o nome do livro: ")
        preco = float(input("Digite o preço do livro: "))
        # na opção 2, depois que a pessoa digitar o nome do livro e depois o preço, o append irá adicioná-los aos arrays devidos
        livros.append(livro)
        precos.append(preco)
        # invoquei a função que vai salvar na lista .txt os livros com seus valores digitados pelo usuário
        salvar_produto_na_lista_de_arquivos()
        print("Livro adicionado com sucesso!")
    elif opcao == "3":
        print("Você finalizou a operação. Rode o arquivo de novo para exibir as opções do menu principal.")
        break
    else:
        print("Opção inválida. Tente novamente.")
