#Faça um programa que leia um número qualquer e mostre o seu fatorial.Ex:$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$
n = int(input('Digite o número para ser cálculado o fatorial: '))
factorial = 1
'''while n != 0:
    factorial = factorial*n
    n = n -1
print('O fatorial é {}'.format(factorial))'''

for n in range(n,0,-1):
    factorial = factorial*n
    n = n -1
print('O fatorial é {}'.format(factorial))