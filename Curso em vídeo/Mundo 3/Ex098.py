#Faça um programa que tenha uma Função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1 b) De 10 até 0, de 2 em 2 c) Uma contagem personalizada.
from time import sleep

def contador(inicio,fim,passo):
    if passo > 0:
        sup = 1
    elif passo < 0:
        sup = -1
    else:
        passo = 1
        sup = 1
    print(f'contagem de {inicio} até {fim} de {passo}')
    for c in range(inicio,fim+sup,passo):
        print(f'{c}', end=' ')
        sleep(0.2)
    print('\nFim da contagem')


contador(1,10,1)
contador(10,0,-2)
contador(int(input('Digite o inicio da contagem: ')),int(input('Digite o fim da contagem: ')), int(input('Digite o passo da contagem: ')))
