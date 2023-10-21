import random

def jogar_advinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    numero_secreto = (random.randrange(1,101)) #numero inteiro entre 1 e 100
    total_tentativas = 0
    pontos = 1000;

    print("Defina um nível: (1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20;
    elif(nivel == 2):
        total_tentativas = 10;
    else:
        total_tentativas = 5;

# contador vai rodar até chegar no valor de total_tentativas, que é 3
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #  ele imprime que o usuário deve 
    #digitar um número ente 1 e 100 e volta pro início do laço pra continuar a rodada


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute);
            pontos = pontos - pontos_perdidos
            # rodada = rodada + 1
            # total_tentativas = total_tentativas - 1 ## para não entrar em loop infinito. Aqui é o incremento ou decremento, no caso do -

        print("Fim do jogo")

if(__name__ == "__main"):
    jogar_advinhacao()
