#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
while True:
    n = int(input("Digite um valor: "))
    if lista.count(n) == 0:
        print('\033[0:32mAdicionado o valor\033[m')
        lista.append(n)
    else:
        print(f'\033[0:31mValor duplicado, não será adicionado\033[m')
    continuar = int(input("Deseja continuar?:\n[1].Sim\n[2].Não\n "))
    if continuar == 2:
        print(f'{lista}')
        break
print(f'Os valores digitados foram \033[0:33m{sorted(lista)}\033[m')
