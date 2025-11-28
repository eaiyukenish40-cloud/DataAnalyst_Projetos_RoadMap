#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
n3 = int(input('Digite sua terceira nota: '))
media = (int(n1) + int(n2) + int(n3))/3
if media >= 7:
    print('Sua média é \033[0:32m{:.2f}\033[m. APROVADO!!!'.format(media))
elif media < 5:
    print('Sua média é \033[0:31m{:.2f}\033[m. REPROVADO!!!'.format(media))
else:
    print('Sua média é \033[0:33m{:.2f}\033[m. Recuperação!'.format(media))