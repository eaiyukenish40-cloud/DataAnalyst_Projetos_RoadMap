#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da sua chapecoense.
from operator import index

times = ('Palmeiras','Flamengo','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','São Paulo','Vasco da Gama','Corinthians','Atlético-MG','Red Bull Bragantino','Ceará','Grêmio','Internacional','Vitória','Santos','Juventude','Fortaleza','Sport')
n = int(input('Veja quais a colocação dos times do campeonato BR. Digite qual opção: \n[1].5°Colocados\n[2].4 últimos colocados\n[3].Lista do time em ordem alfabética\n[4].Qual posição está o Santos\n'))
if n == 1:
    print(f'Os 5° colocados são:\n{times[0:5]}')
elif n == 2:
    print('Os 4 últimos colocados são:')
    for c in range(-4,0,1):
                print(f'{times[c]}')
elif n == 3:
    print(sorted(times))
elif n == 4:
    print(f'O \033[0:33mSantos\033[m está na {times.index('Santos')+1}° posição')