#Adapte o código do desafio 107 (módulo moeda.py), criando uma Função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
import moeda

n = float(input('Digite um valor: '))
p = float(input('Digite um valor percentual: '))
a = moeda.aumentar(n,p)
print(f'O valor {moeda.moeda(n,'S')}, terá o seu valor aumentado em {p}%. Resultando em: {moeda.moeda(a,'S')} ')
d = moeda.diminuir(n,p)
print(f'O valor {moeda.moeda(n,'S')}, terá o seu valor diminuído em {p}%. Resultando em: {moeda.moeda(d,'S')} ')
dd = moeda.dobro(n)
print(f'O valor dobrado de {moeda.moeda(n,'S')} é {moeda.moeda(dd,'S')}')
print(f'A metade do valor {moeda.moeda(n,'S')} é {moeda.moeda((moeda.metade(n)),'S')}')