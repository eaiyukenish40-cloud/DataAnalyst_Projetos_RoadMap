#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from itertools import count
from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()
rank = {}
count = 0
jogador = {'jogador 1': randint(1, 6),
            'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6),
           'jogador 4': randint(1, 6),}
print('\033[0:33mJogando dado...\033[m')

'''if c == 1:
    maior = jogador['Dado']
    menor = jogador['Dado']
if jogador['Dado'] > maior:
    maior = jogador['Dado']
elif jogador['Dado'] < menor:
    menor = jogador['Dado']'''
for k,v in jogador.items():
    print(f'\033[0:32m{k}\033[m: {v}')
    sleep(1)
rank = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print(rank)
for c,v in enumerate(rank):
    print(f'O {c+1}° lugar é o \033[0:32m{rank[c][0]}\033[m: com {rank[c][1]}')
    sleep(1)
