#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import choice, randint
vitoria = 0
while True:
    pcnum = randint(0,10)
    player = int(input('Digite:\n[1].Par\n[2].Ímpar\n '))
    while player != 1 and player != 2:
        player = int(input('\033[0:31mOpção inexistente.\033[m Digite:\n[1].Par\n[2].Ímpar\n '))
    playernum = int(input('Digite um número de 0 a 10: '))
    print(f'Joguei: {pcnum}')
    soma = playernum + pcnum
    if soma % 2 == 0: #par
        if player == 1:
            print('\033[0:32mVitória\033[m')
            vitoria += 1
        else:
            break
    else: #impar
        if player == 2:
            print('\033[0:32mVitória\033[m')
            vitoria += 1
        else:
            break
print(f'\033[0:31mVocê perdeu\033[m.O seu número de vitórias foi \033[0:33m{vitoria}\033[m.')