#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = float(input('Digite um valor: '))
    lista.append(n)
    lista.sort(reverse=True)

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[0:33mOpção inválida.\033[mQuer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
if lista.count(5) == 0:
    print('\033[0:31mO valor 5 não foi digitado e não está na lista.\033[m')
else:
    print('\033[0:32mO valor 5 foi digitado e está na lista.\033[m')
print(f'Os números digitados foram \033[0:32m{lista}\033[m. Temos \033[0:32m{len(lista)}\033[m números digitados.')