#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
n = int(input('Digite o 1° número de uma progressão aritmética: '))
r = float(input('Digite sua razão: '))
soma = n
PA = []
PA2 = []
c = 0
rota = 0
rota2 = 0
texto = ''
while c < (10 + rota):
    if rota == 0 and rota2 == 0:
        PA.append(soma)
    else:
        PA2.append(soma)
        texto = 'Os termos novos são \033[0:33m{}\033[m'.format(PA2)
    soma = soma + r
    c += 1
    if c == 10:
        if rota == 0 and rota2 == 0:
            print('Os termos dessa P.A. são {}'.format(PA))
        elif rota == 0 and rota2 != 0:
            print(texto)
        rota = int(input('Rota 1:Deseja mostra mais termos? Digite a quantidade: '))
    if rota != 0 and c >= 10 + rota:
        print(texto)
        rota2 = int(input('Rota2:Deseja mostra mais termos? Digite a quantidade: '))
        if rota2 != 0:
            c = c - rota - rota2
            rota = 0
print('Todos os termos dessa P.A. são \033[0:32m{}\033[m. {}'.format(PA,texto))