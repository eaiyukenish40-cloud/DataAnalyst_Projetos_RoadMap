#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
#[][][]
#[][][]
#[][][]
lista = []
matriz = list()
for c in range(0,9):
    n = int(input('Digite um valor: '))
    matriz.append(n)
    lista.append(matriz[:])
    matriz.clear()
for c in range(0,3):
    print(f'{lista[c]}{lista[c+1]}{lista[c+2]}\n',end='')
