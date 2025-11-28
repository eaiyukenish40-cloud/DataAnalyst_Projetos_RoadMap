#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

count = soma = media = n = 0
decisão = 1
num = []
while decisão == 1:
    n = int(input('Digite um número: '))
    soma += n
    count += 1
    num.append(n)
    decisão = int(input('Deseja continuar?\n[1].Sim\n[2].Não\n '))
    while decisão != 1 and decisão != 2:
        decisão = int(input('\033[31mOpção inexistente\033[m. Deseja continuar?\n[1].Sim\n[2].Não\n '))
media = soma / count
print('A média resultante é {:.2f}, o maior valor é {}, o menor é {}'.format(media,max(num), min(num)))