'💡 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'
print('Digite o valor em metros que você quer a conversão')
n1 = float(input('Digite um valor: '))
centimetro = n1 * 100
milimetro = n1 * 1000
print('O valor de {}m representa {}cm e {}mm'.format(n1, centimetro, milimetro))