#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
n = 0
par = []
soma = 0
for c in range(1,500+1):
    if c % 3 == 0 and c % 2 != 0:
        par.append(c)
        n = n + 1
        soma = soma + c
print('Os números multiplos de 3 são {}.\nHá no total \033[0:32m{}\033[m números múltiplos e sua soma é {}'.format(par,n,soma))