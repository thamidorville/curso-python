import forca
import advinhacao

def escolher_jogo():
    print("*********************************")
    print("Escolha seu Jogo:")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando advinhação")
        advinhacao.jogar_advinhacao()

if(__name__ == "__main__"):
    escolher_jogo()