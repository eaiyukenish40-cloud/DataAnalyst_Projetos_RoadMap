#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date

def voto (nas):
    global idade
    idade = date.today().year - nas

    if idade < 16:
        status = 'Negado'
    elif 16 <= idade < 18 or idade > 65:
        status = 'Opcional'
    else:
        status = 'Obrigatório'
    return status


n = int(input('Digite o ano de nascimento: '))
voto(n)
print(f'Você tem \033[0:33m{idade}\033[m anos. Seu status de votação é \033[0:32m{voto(n)}\033[m')