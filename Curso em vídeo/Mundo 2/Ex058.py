# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0,10)
user = int(input('Digite seu número de jogador (0 a 10): '))
count = 1
cor = ''
while user != pc:
    if user < pc:
        user = int(input('\033[0:31mErrou...\033[m o numero é maior. Tente mais uma vez: '))
    else:
        user = int(input('\033[0:31mErrou...\033[m o numero é menor. Tente mais uma vez: '))
    count += 1
if count <= 2:
    cor = '\033[32m'
elif count > 3 and count < 5:
    cor = '\033[33m'
elif count > 5:
    cor = '\033[31m'
print('\033[0:32mAeee. Acertou.\033[m Suas tentativas foram: {}{}\033[m'.format(cor,count))