'💡 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('O triangulo de cat op. {} e cat adj. {} possui uma hipotenusa {}'.format(co, ca,hip))