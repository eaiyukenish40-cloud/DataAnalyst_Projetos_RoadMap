'Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.'
tc = float(input('Digite a temperatura: C°'))
tf = tc*(9/5)+32
print('A temperatura de C°{} em Fahreint é de F°{:.2f}'.format(tc, tf))