#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
tupla = (random.sample(range(0, 101), 5))
print(f'Os valores gerados são \033[0:33m{tupla}\033[m.Sendo o maior \033[0:33m{max(tupla)}\033[m e o menor \033[0:33m{min(tupla)}')