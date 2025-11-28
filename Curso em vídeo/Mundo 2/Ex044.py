#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJAS DR. FOOL'))
valor = float(input('Qual o valor do produto? '))
pagamento = int(input('\033[0:33mQual a forma de pagamento?\033[m\n[1.]À vista dinheiro/cheque: 10% desconto\n[2.]À vista no cartão: 5% de desconto\n[3.]2x no cartão: sem desconto\n[4.]3x ou mais no cartão: 20% de juros\n'))
if pagamento == 1:
    print('Você escolheu \033[0:32mà vista no dinheiro ou cheque e terá 10% de desconto\033[m. Pagando R$ {:.2f}'.format(valor*0.90))
elif pagamento == 2:
    print('Você escolheu \033[0:32mà vista no cartão e terá 5% de desconto\033[m. Pagando R$ {:.2f}'.format(valor * 0.95))
elif pagamento == 3:
    print('Você escolheu \033[0:32mpagamento parcelado em 2x no cartão\033[m. \033[0:31mNão há desconto\033[m. Pagando \033[0:33mR$ {:.2f}\033[m no total com \033[0:33m2 parcelas de R${}\033[m.'.format(valor, valor / 2))
elif pagamento == 4:
    n = int(input('Qual o número de parcelas? '))
    print('Você escolheu \033[0:32mpagamento parcelado em 3x ou mais no cartão\033[m.\033[0:33m Pagando 20% de juros\033[m. R$ {:.2f} no total com {} parcelas sendo cada .'.format(valor * 1.2,n,valor*1.2/n))
else:
    valor = 0
    print('\033[0:31mOpção invalida!\033[m. Não é possível seguir com sua compra.')