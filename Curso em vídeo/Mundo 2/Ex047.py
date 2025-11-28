#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
n = 0
par = []
for c in range(1,50+1):
    if c % 2 == 0:
        print('\033[0:33m{}\033[m é \033[0:33mPAR\033[m'.format(c))
        par.append(c)
        n = n + 1
print('Os números pares são {}. Há no total \033[0:32m{}\033[m números pares'.format(par,n))