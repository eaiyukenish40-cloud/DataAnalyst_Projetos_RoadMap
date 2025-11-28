#Aprimore o desafio anterior (criação e preenchimento de uma matriz $3 x 3$), mostrando no final:A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.
lista = []
matriz = list()
soma = maior = 0
for c in range(0,9):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
    if c == 3:
        maior = n
    if n > maior and c > 3 and c < 6: # pega o maior da valor da 2° coluna
        maior = n
    matriz.append(n)
    lista.append(matriz[:])
    matriz.clear()
print(f'A soma dos valores pares digitados = \033[0:32m{soma}\033[m')
print(f'O maior valor da 2° linha é \033[0:32m{maior}\033[m')
soma = 0
n = 0
for c in range(0,3):
    if n != 0:
        n += 2
    print(f'{lista[n]}{lista[n+1]}{lista[n+2]}\n',end='')
    n += 1
    if c == 2:
        soma = lista[c+1][0] + lista[c+3][0] + lista[c+2][0]
print(f'A soma dos valores da 2° linha são: \033[0:32m{soma}\033[m')
