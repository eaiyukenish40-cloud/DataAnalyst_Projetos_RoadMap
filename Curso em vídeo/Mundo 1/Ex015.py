'Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R60 por diae R0.15 por Km rodado'
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de Km rodado: '))
print('Considerando a quantidade de {} dias e {}km percorridos, o valor total a pagar é de R${:.2f}'.format(dias, km, km * 0.15 + dias*60))