#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*n):
    maior = 0
    print(f'Todos os valores: {n}')
    for c,v in enumerate(n):
        count += 1
        if c == 0:
            maior = v
        if v > maior:
            maior = v
    print(f'O maior dos valores é {maior}')
    print(f'Foram lidos {len(n)} valores')


maior(2,3,4,5,6,7,8,9,10,56,122,123,564,33,213,5678,1231,442,2234)