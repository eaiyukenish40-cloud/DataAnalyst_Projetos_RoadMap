#Crie um programa que tenha uma função Fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do Fatorial.
def fatorial(n,show = False):
    f = 1
    for c in range(n,0,-1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c}x',end='')
            else:
                print(f'1 = ',end='')
    return f

n = int(input('Digite o número que deseja calcular o fatorial: '))
calculo = ''
while calculo != 'S' and calculo != 'N':
    calculo = str(input('Deseja ver o cálculo? [S/N]: ')).strip().upper()[0]
    if calculo == 'N':
        calculo = False
        break
    if calculo == 'S':
        calculo = True
        break
fatorial(n, calculo)
print(f'{fatorial(n)}')