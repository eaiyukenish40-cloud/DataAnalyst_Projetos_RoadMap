#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos_casa = int(input('Quantos anos de financiamento? '))
mensalidade = valor_casa / (anos_casa*12)
if 0.3*salario < mensalidade:
    print('Infelizmente o seu salário de \033[1:31mR${:.2f}\033[m não é aprovado para o valor das mensalidades de \033[0:31mR${:.2f}\033[m'.format(salario, mensalidade))
else:
    print('\033[0:1:32mEmpréstimo aprovado!\033[mAs mensalidades de \033[0:32mR${:.2f}\033[m são compatíveis com o seu salário!'.format(mensalidade))