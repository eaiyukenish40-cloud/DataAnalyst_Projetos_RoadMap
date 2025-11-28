#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
maior = menor = pos = 0
lista = []
for c in range(0, 5):
    n = float(input('Digite um valor: '))
    if c == 0:
        maior = menor = n
        lista.append(n)
        pos = c
    if n > maior:
        maior = n
        lista.append(n)
    else:
        if n < menor:
            menor = n
            lista.insert(pos, n)
        elif n < maior and c != 0:
            for a,v in enumerate(lista):
                 if n < v:
                    lista.insert(a, n)
                    break
print(lista)
