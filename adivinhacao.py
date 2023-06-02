import random

def jogar():

    numero_secreto = random.randrange(1, 51) 

    print(numero_secreto)
    print("bem-vindo ao jogo da adivinhação")
    print("escolha a dificuldade", "[1]Fácil, [2]Médio, [3]Difícil", sep='\n')

    dificuldade = int(input("qual o nível? "))


    total_de_tentativas = 0

    pontos = 100


    if(dificuldade == 1):
        print("você escolheu, fácil")
        total_de_tentativas = 10
    elif(dificuldade == 2):
        print("você escolheu, médio")
        total_de_tentativas = 5
    elif(dificuldade == 3):
        print("você escolheu difícil")
        total_de_tentativas = 3
    else:
        print("escolha entre 1, 2 ou 3")
        
    #for in range(start, stop, [step])
    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("digite um número entre 1 e 50 ")  
        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 50):
            print("número inválido")
            continue

    

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print ("Você acertou!", "pontuação {}".format(pontos))
            break
        else:
            if(maior):
                print("Errado, o número é menor")
            elif(menor):
                print("Errado, o número é maior")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()