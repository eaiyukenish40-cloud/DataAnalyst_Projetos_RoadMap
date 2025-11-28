#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogo = list()
n = int(input('Quantos jogos deseja sortear? '))
print('\033[0:32mSORTEANDO...\033[m')
for c in range(0,n):
    count = repeticao = 0
    sleep(1)
    for a in range(0,6):
        v = randint(1,60)
        if count == 0:
            jogo.append(v)
        else:
            for m in jogo: # if v not in jogo - poderia ter evitado esse laço for
                if m == v:
                    while v == m:
                        #repeticao += 1
                        v = randint(1,60)
                        #print(f'a repetição foi de {repeticao}')
            jogo.append(v)
        count = 1

    print(f'O {c+1}° jogo é: {jogo[:]}')
    jogo.clear()
print('Boa sorte!')
