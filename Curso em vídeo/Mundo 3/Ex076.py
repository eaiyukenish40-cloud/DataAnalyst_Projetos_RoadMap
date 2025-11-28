#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = ('caderno','R$ 15.50','mochila','R$ 89.90','borracha','R$ 1.50','régua','R$ 3.75','apontador','R$ 2.25','tesoura','R$ 7.00','cola','R$ 4.50','estojo','R$ 18.00','lápis de cor','R$ 25.99','canetinha','R$ 19.99')
count = 0
for c in range(0,len(tupla)):
    if c+1+count == len(tupla)-1:
        break
    print(f'{tupla[c+count]:.<30}{tupla[c+1+count]} ')
    count += 1

