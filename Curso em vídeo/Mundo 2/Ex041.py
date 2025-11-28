#A Confederação Nacional da Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
from datetime import date
ano = int(input('Qual o ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria \033[0:31mMirim\033[m: \033[0:34midade {}\033[m'.format(idade))
elif idade > 9 and idade <= 14:
    print('Categoria \033[0:31mInfantil\033[m: \033[0:34midade {}\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('Categoria \033[0:31mJunior\033[m: \033[0:34midade {}\033[m'.format(idade))
elif idade > 19 and idade <= 20:
    print('Categoria : \033[0:31mSenior\033[m: \033[0:34midade {}\033[m'.format(idade))
else:
    print('Categoria \033[0:31mMaster\033[m: \033[0:34midade {}\033[m'.format(idade))