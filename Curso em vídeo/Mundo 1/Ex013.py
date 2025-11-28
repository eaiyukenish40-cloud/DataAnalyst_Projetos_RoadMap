'💡 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'
n1 = float(input('Digite o seu salário: '))
print('O seu salário R${} terá um aumento de 15% que equivale a R${:.2f}, sendo o valor total de R${:.2f}'.format(n1,n1*0.15,n1*1.15))