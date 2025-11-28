#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('\033[0:33mVamos jogar um joken-po?\033[m')
sleep(0.5)
print('.'*10)
sleep(1)
pc = random.choice(['Pedra','Papel','Tesoura'])
valor = int(input('Escolha:\n1.Papel\n2.Tesoura\n3.Pedra\n4.Sair(qualquer valor)\n '))
if valor == 1:
    jogo = 'Papel'
elif valor == 2:
    jogo = 'Tesoura'
elif valor == 3:
    jogo = 'Pedra'
sleep(0.5)
print('.'*10)
print( 'Seu adversário escolheu \033[0:33m{}\033[m'.format(pc))
sleep(1)
if (jogo == 'Pedra' and pc == 'Pedra') or (jogo == 'Papel' and pc == 'Papel') or (jogo == 'Tesoura' and pc == 'Tesoura'):
    print('Houve um empate')
elif (jogo == 'Pedra' and pc == 'Tesoura') or (jogo == 'Papel' and pc == 'Pedra') or (jogo == 'Tesoura' and pc == 'Papel'):
    print('\033[0:32mVocê ganhou!!!\033[m')
elif (jogo == 'Pedra' and pc == 'Papel') or (jogo == 'Papel' and pc == 'Tesoura') or (jogo == 'Tesoura' and pc == 'Pedra'):
    print('\033[0:31mVocê perdeu...\033[m')

