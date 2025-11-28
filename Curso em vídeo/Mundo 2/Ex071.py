#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# 1OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
texto50 =texto20 = texto10 = texto1 = ''
operacao = 0
while True:
    saque = int(input('Qual o valor de saque? '))
    notas50 = saque // 50
    notas20 = saque // 20
    notas10 = saque // 10
    notas1 = saque // 1
    decisao = input('Deseja seguir com saque otimizado? [S/N] ').upper().strip()
    if decisao == 'S':
        if notas50 !=0:
            valor = saque - notas50*50
            if notas50 != 0:
                texto50 = f'-O número de notas de 50$ é \033[0:32m{notas50}\033[m'
        if notas20 != 0:
            notas20 = valor//20
            valor = valor - notas20*20
            if notas20 != 0:
                texto20 = f'-O número de notas de 20$ é \033[0:32m{notas20}\033[m'

        if notas10 != 0:
            notas10 = valor // 10
            valor = valor - notas10*10
            if notas10 != 0:
                texto10 = f'-O número de notas de 10$ é \033[0:32m{notas10}\033[m'

        if notas1 != 0 and valor != 0:
            notas1 = valor // 1
            valor = valor - notas1*1
            if notas1 != 0:
                texto1 = (f'-O número de notas de 1$ é \033[0:32m'
                          f'{notas1}\033[m')

        print(f'\033[0:33mTotal:\033[m \n{texto50}\n{texto20}\n{texto10}\n{texto1}')
        operacao += 1
        notas50 = notas20 = notas10 = notas1 = 0
        texto50 = texto10 = texto1 = texto20 = ''
    elif decisao == 'N':
        if notas50 != 0:
            print(f'É possível pegar {notas50} de R$50')
            qtde = int(input('Quantas notas deseja sacar? '))
            texto50 = f'-O número de notas de 50$ é \033[0:32m{qtde}\033[m'
            valor = saque - qtde * 50
            notas20 = valor // 20
        if notas20 != 0:
            print(f'É possível pegar {notas20} de R$20')
            qtde = int(input('Quantas notas deseja sacar? '))
            texto20 = f'-O número de notas de 20$ é \033[0:32m{qtde}\033[m'
            valor = valor - qtde * 20
            notas10 = valor // 10
        if notas10 != 0:
            print(f'É possível pegar {notas10} de R$10')
            qtde = int(input('Quantas notas deseja sacar? '))
            texto10 = f'-O número de notas de 10$ é \033[0:32m{qtde}\033[m'
            valor = valor - qtde * 10
            notas1 = valor // 1
        if notas1 != 0:
            print(f'É possível pegar {notas1} de R$1')
            qtde = int(input('Quantas notas deseja sacar? '))
            texto1 = f'-O número de notas de 1$ é \033[0:32m{qtde}\033[m'
            valor = valor - qtde * 1
        print(f'Você sacou \033[0:32mR${saque-valor}\033[m. Sendo:\n{texto50}\n{texto20}\n{texto10}\n{texto1}')
        operacao += 1
        notas50 = notas20 = notas10 = notas1 = 0
        texto50 = texto10 = texto1 = texto20 = ''
    else:
        print('Erro...saindo')
        break

