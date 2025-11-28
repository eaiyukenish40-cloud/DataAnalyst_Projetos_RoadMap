#Faça um programa que tenha uma Função chamada Área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l,c):
    a = l * c
    print(f'A área do terreno é \033[0:33m{a}\033[m')

area(int(input('Informe a largura do terreno: ')),int(input('Informe o comprimento do terreno: ')))