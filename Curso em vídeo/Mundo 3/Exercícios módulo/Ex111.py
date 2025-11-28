#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote (moeda) e mantenha tudo funcionando.
from utilidadesCeV import dado,moeda
n = float(input('Digite um valor: '))
p = float(input('Digite um valor percentual aumento: '))
m = float(input('Digite um valor percentual queda: '))
moeda.resumo(n,p,m)