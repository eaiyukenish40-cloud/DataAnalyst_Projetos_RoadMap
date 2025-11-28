#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
operacao = 0
while operacao != 5:
    operacao = int(input('\033[0:33mEscolha uma opção:\n[1].Soma\n[2].Multiplicar\n[3].Maior\n[4].Novos Números\n[5].Sair do programa\033[m\n'))
    if operacao == 1:
        resultado = n1 + n2
        print('\033[1;31mO resultado da soma será {}:\033[m'.format(resultado))
    elif operacao == 2:
        resultado = n1 * n2
        print('\033[1;31mO resultado da multiplicação será {}:\033[m'.format(resultado))
    elif operacao == 3:
        resultado = max(n1, n2)
        print('\033[1;31mO maior número é {}:\033[m'.format(resultado))
    elif operacao == 4:
        n1 = float(input('Digite novamente o 1° valor: '))
        n2 = float(input('Digite novamente o 2° valor: '))
        operacao = 0
    elif operacao == 5:
        print('Obrigado por utilizar o programa!')
    else:
        operacao = 0
        print('\033[31mOperação inválida, tente novamente\033[m')

