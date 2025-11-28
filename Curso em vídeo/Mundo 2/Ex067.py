#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Qual tabuada deseja ver: '))
    if  n < 0:
        print('Encerrando...')
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
