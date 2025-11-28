#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
n = float(input('Digite um valor: '))
p = float(input('Digite um valor percentual: '))
a = moeda.aumentar(n,p)
print(f'O valor {n}, terá o seu valor aumentado em {p}%. Resultando em: {a:.2f} ')
d = moeda.diminuir(n,p)
print(f'O valor {n}, terá o seu valor diminuído em {p}%. Resultando em: {d:.2f} ')
dd = moeda.dobro(n)
print(f'O valor dobrado de {n} é {dd}')
print(f'A metade do valor {n} é {moeda.metade(n)}')