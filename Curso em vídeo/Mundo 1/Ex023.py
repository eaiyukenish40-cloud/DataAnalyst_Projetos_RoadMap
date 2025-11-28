'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''
#num = str(input('Digite um número de 0 a 9999: ')).strip()
#print('Analisando...\n O número {} tem sua suas separações em \n Unidade: {} \n Dezena {} \n Centena {} \n Milhar {} \n'.format(num, num[3], num[2], num[1], num[0]))
numbers = int(input('Digite um numero: '))
u = numbers // 1 % 10
d = numbers // 10 % 10
c = numbers // 100 % 10
m = numbers // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
