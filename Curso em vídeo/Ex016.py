'💡 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.'
'Ex:Digite um número: 6.127'
'O número 6.127 tem a parte inteira 6.'
import math
n = float(input('Digite um número: '))
n2 = int(n)
print('A parte inteira do número {} é {}'.format(n, n2))
'era possível usar o metodo trunc'
print('A parte inteira do numero {} é {}'.format(n, math.trunc(n)))