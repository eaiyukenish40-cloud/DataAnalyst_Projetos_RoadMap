#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda
n = float(input('Digite um valor: '))
p = float(input('Digite um valor percentual aumento: '))
a = moeda.aumentar(n,p)
formato = ''
while formato != 'S' and formato != 'N':
    formato = str(input('Deseja formatar o valor? [S/N] ')).strip().upper()
print(f'O valor {moeda.moeda(n,formato)}, terá o seu valor aumentado em {p}%. Resultando em: {moeda.moeda(a,formato)} ')
m = float(input('Digite um valor percentual queda: '))
d = moeda.diminuir(n,m)
print(f'O valor {moeda.moeda(n,formato)}, terá o seu valor diminuído em {m}%. Resultando em: {moeda.moeda(d,formato)} ')
dd = moeda.dobro(n)
print(f'O valor dobrado de {moeda.moeda(n,formato)} é {moeda.moeda(dd,formato)} ')
print(f'A metade do valor {moeda.moeda(n,formato)} é {moeda.moeda((moeda.metade(n)),formato)}')