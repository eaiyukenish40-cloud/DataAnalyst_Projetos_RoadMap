#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_pares = []
lista_impares = []
while True:
    n = float(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[0:33mOpção inválida.\033[mQuer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        print('\033[0:31mSaindo...\033[m')
        break
print(f'Verificando numeros pares e impares da lista{lista}')
for c, v in enumerate(lista):
    print(v)
    print('Entrando no loop')
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)
print(f'A lista digitada foi {lista}. Os valores pares são \033[0:33m{lista_pares}\033[m e os valores ímpares \033[0:33m{lista_impares}\033[m')