import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Adivinhação unt (2) Adivinhação melhor")

    jogo = int(input("Qual o jogo você quer jogar?"))

    if (jogo == 1):
        print("Esse não mano")
        forca.jogar()
    elif (jogo == 2):
        print ("Você escolheu jogo da adivinhação!")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()