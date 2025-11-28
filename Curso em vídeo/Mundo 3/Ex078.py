#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
maior = menor = pos_menor = pos_maior = 0
for c in range(0, 5):
    lista.append(float(input('Digite um valor: ')))
    if c  == 0:
        maior = menor = lista[0]
    if lista[c] > maior:
        maior = lista[c]
        #pos_maior = c + 1
    elif lista[c] < menor:
        menor = lista[c]
        #pos_menor = c + 1
print(f'A lista digitada foi \033[0:33m{lista}\033[m.')
print(f'O maior valor foi \033[0:33m{maior}\033[m. E apareceu nas posições: ',end='')
for c,v in enumerate(lista):
    if v == maior:
        print(f'{c+1}', end='...')
print(f'O menor valor foi \033[0:33m{menor}\033[m. E apareceu nas posições: ',end='')
for c,v in enumerate(lista):
    if v == menor:
        print(f'{c+1}', end='...')

