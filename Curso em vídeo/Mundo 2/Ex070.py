#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000. C) Qual é o nome do produto mais barato.
soma = count = menor = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().lower().capitalize()
    preco = float(input('Digite o valor do produto: '))
    soma = soma + preco
    if menor == 0:
        menor = preco
        barato = nome
        print('\033[0:33mPassou por esse loop\033[m',menor)
    if preco > 1000:
        count += 1
    if preco < menor:
        menor = preco
        barato = nome
    continuar = int(input('Deseja continuar? \n[1].Sim \n[2].Não\n'))
    while continuar != 2 and continuar != 1:
        continuar = int(input('\033[0:31mOpção inválida\033[m.Deseja continuar? \n[1].Sim \n[2].Não\n'))
    if continuar == 2:
        print('\033[0;30;41mProcesso encerrado\033[m')
        break
print(f'O total da compra foi \033[0:33m{soma}\033[m. O número de produtos que custam mais de R$1000 é \033[0:32m{count}\033[m. O produto mais barato é \033[0:33m{barato}\033[m.')

