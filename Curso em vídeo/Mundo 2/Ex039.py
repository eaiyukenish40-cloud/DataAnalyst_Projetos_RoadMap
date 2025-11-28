#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year

idade = int(input('Digite seu ano de nascimento: '))
if atual-idade < 18:
    print('Você ainda tem \033[0:32m{}\033[m anos e vai precisar se alistar para o serviço militar daqui a {} ano(s)'.format(atual-idade,atual- idade - 18))
elif atual-idade == 18:
    print('Você já tem \033[0:32m{}\033[m anos e é hora de se alistar para o serviço militar'.format(atual-idade))
else:
    print('Você tem \033[0:32m{}\033[m anos. Já passou da idade se alistar para o serviço militar. Caso não tenha ido, vá imediatamente regularizar essa situação'.format(atual-idade))

