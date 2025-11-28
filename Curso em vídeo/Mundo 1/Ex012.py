'💡 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'
n1 = float(input('Digite o preço de um produto: '))
nf = n1*0.95
print('O valor final do produto com 5% de desconto é de: R${:.2f}'.format(nf))