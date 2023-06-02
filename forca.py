def jogar():

    boas_vindas = "jogo da adivinhação"

    print ("bem vindo ao", boas_vindas, end="\n")

    numero_secreto = 42
    total_de_tentativas = 3
    rodada = 1

    while (total_de_tentativas > 0): 
        print("tentativa {} resta {}".format(rodada, total_de_tentativas))
        rodada += 1
        chute = input("digite o seu número: ")
        numero = int(chute)

        print ("você digitou ", chute) 

        if (numero_secreto == numero):
            total_de_tentativas = 0
            print("Você acertou!")
        else:
            if(numero_secreto < numero):
                print("Errado o número é menor")
            elif(numero_secreto > numero):
                print("Errado o número é maior")
        total_de_tentativas -= 1 
        if (total_de_tentativas == 0):
            print('Fim de jogo')

if (__name__ == "__main__"):
    jogar()

