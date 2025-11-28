'💡 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.'
'Considere US1.00=R3.27'
n1 = float(input('Digite quantos R$ você possui na carteira: '))
dolar = n1 / (3.27)
print('O valor R${:.2f}, na atual cotação do dolar R$3,27, equivalem a ${:.2f}'.format(n1,dolar))
