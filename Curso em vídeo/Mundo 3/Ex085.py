#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = list()
pares = list()
impares = list()
for c in range(0,7):
    n = int(input('Digite um n°: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)
print(f'Os valores apresentados são {lista}')