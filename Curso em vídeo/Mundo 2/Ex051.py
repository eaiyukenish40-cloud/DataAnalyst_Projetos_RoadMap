# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.
n = int(input('Digite o 1° número de uma progressão aritmética: '))
r = float(input('Digite sua razão: '))
soma = n
PA = []
for c in range(1,10+1):
    PA.append(soma)
    soma = soma + r
print('Os termos dessa P.A. são {}'.format(PA))