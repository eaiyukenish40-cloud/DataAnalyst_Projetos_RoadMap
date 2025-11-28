#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA (Progressão Aritmética), mostrando os 10 primeiros termos da progressão usando a estrutura while.
n = int(input('Digite o 1° número de uma progressão aritmética: '))
r = float(input('Digite sua razão: '))
soma = n
PA = []
c = 0
while c < 10:
    PA.append(soma)
    soma = soma + r
    c += 1
print('Os termos dessa P.A. são {}'.format(PA))