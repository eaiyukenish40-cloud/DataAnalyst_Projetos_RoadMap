#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0→1→1→2→3→5→8→…
n = int(input('Quantos termos deseja mostrar da sequência de fibonacci? : '))
a1 = 0
a2 = 1
a3 = 0
count = 2
print(a1, a2, end=' ')
while n > count:
    count += 1
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print(a3, end=' ')

