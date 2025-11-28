#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada (Flag).
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o Flag).

count = soma = n = 0
while True:
    soma += n
    count += 1
    n = int(input('Digite um número (para parar digite 999): '))
    if n == 999:
        break
print(f'Você digitou \033[0:33m{count}\033[m números e a soma total deles é \033[0:33m{soma}\033[m')