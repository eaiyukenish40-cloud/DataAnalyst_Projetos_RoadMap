'💡 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'
import math
from math import degrees

n = float(input('Digite o valor do angulo (graus) a ser trabalhado: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O valor do angulo escolhido tem seu sen = {:.2f}, cos = {:.2f} e tang = {:.2f}'.format(sen, cos, tan))
