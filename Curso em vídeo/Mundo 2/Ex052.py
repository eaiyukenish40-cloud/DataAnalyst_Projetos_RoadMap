#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite o número inteiro: '))
count = 0
for c in range(1,n+1):
    if n % c == 0:
        count = count + 1
        if count > 2 or n == 1 or n == 0:
            print('O {} não é primo'.format(n))
            break
if count == 2:
    print('O número {} é primo'.format(n))