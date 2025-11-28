# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
from itertools import count

soma = 0
count = 0
pares = []
for c in range(0,6):
    n = int(input('Digite o {}° número: '.format(c+1)))
    if n % 2 == 0:
        soma = soma + n
        pares.append(n)
        count += 1
print('O resultado da soma dos números pares digitados {} \né {}. Temos {} pares'.format(pares,soma,count))