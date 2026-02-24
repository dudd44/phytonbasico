import random
print('********************')
print('**Jogo adivinhação**')
print('********************')

print('1 - FÁCIL')
print('2 - MÉDIO')
print('3 - DIFÍCIL')

opcao = int(input("Escolha uma opção: "))

print("Você escolhe a opção: " , opcao)
if (opcao ==1):
    total_tentativas = 15
elif (opcao ==2):
    total_tentativas = 10
elif (opcao ==3):
    total_tentativas = 5

numero_secreto = random.randrange(1,50)

for rodada in range(1, total_tentativas +1):
    print("Tentativas {} de {}".format(rodada,total_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Seu número é: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 30!")

    acertou = chute == numero_secreto 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você Acertou!")
        break
    else:
        if(maior):
            print("******O seu chute foi maior que o número secreto******",)
        elif(menor):
            print("******O seu chute foi menor que o número secreto******")

print("Fim de jogo!") 