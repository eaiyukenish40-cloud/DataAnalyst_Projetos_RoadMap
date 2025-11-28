'💡 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'
A = float(input('Digite a altura da parede(m): '))
L = float(input('Digite a largura da parede(m): '))
AA = A*L
litros = AA/2
print('Uma área de Altura {}m e Lagura {}m, será de {}m^2, e a quantidade de tinta necessária será de {}L '.format(A,L,AA,litros))