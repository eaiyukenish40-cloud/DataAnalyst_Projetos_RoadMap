#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = ()
c = 0
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite outro valor: '))
n4 = float(input('Digite outro valor: '))
tupla = (n1, n2, n3, n4)
if n1 % 2 == 0:
    c += 1
elif n2 % 2 == 0:
    c += 1
elif n3 % 2 == 0:
    c += 1
elif n4 % 2 == 0:
    c += 1
print(f'O 9 apareceu \033[0:33m{tupla.count(9)}\033[m vezes. O 1° digito 3 apareceu na posição {tupla.index(3)+1}. Temos {c} números pares.')