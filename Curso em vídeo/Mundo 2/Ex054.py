#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
count = 0
count_menor = 0
idades_maior = []
idades_menor = []
for c in range(0,7):
    n = int(input('Digite ano de nascimento: '))
    if atual - n >= 18:
        count = count + 1
        idades_maior.append(atual - n)
    else:
        idades_menor.append(atual - n)
        count_menor = count_menor + 1
print('Temos \033[0:33m{}\033[m pessoas de maior idade, \033[0:33m{}\033[m de menor idade.'.format(count, count_menor))
print('As idades de maior são: \033[0:33m{}\033[m \nAs idades de menor são: \033[0:33m{}\033[m'.format(idades_maior, idades_menor))
