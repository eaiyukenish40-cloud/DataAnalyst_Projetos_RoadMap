#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
comparador = 0
count_ref = 0
for c in range(0,6):
    peso = float(input('Digite seu peso: '))
    comparador = peso
    if count_ref == 0:
        menor = comparador
        maior = comparador
        count_ref = count_ref + 1
    if comparador > maior:
        maior = comparador
    else:
        if comparador < menor:
            menor = comparador
print('O maior peso é {} e o menor é {}'.format(maior, menor))