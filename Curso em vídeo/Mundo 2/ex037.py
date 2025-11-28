#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
base = int(input('Escolha sua base: \n\033[0:31m1.Binário \n2.Octal \n3.Hexadecimal\033[m \n'))
if base != 1 and base != 2 and base != 3:
    print('Você não escolheu uma opção válida.')
else:
    if base == 1: #binário
        nome = 'Binário'
        conversao = bin(n)
        print('A base que você escolheu é a \033[0:31m{}\033[m. E o número \033[0:31m{}\033[m, convertido é: \033[0:32m{}\033[m'.format(nome, n, conversao[2:]))
    elif base == 2: #octal
        nome = 'Octal'
        conversao = oct(n)
        print('A base que você escolheu é a \033[0:31m{}\033[m. E o número \033[0:31m{}\033[m, convertido é: \033[0:32m{}\033[m'.format(nome, n, conversao[2:]))
    elif base == 3: #hexa
        nome = 'Hexadecimal'
        conversao = hex(n)
        print('A base que você escolheu é a \033[0:31m{}\033[m. E o número \033[0:31m{}\033[m, convertido é: \033[0:32m{}\033[m'.format(nome, n, conversao[2:]))
