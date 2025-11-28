#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
l1 = int(input('Digite o primeiro lado do triangulo: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com essas medidas temos um triangulo.', end = '')
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('Ele é \033[0:34misóceles')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Ele é \033[0:34mEquilatero')
    else:
        print('Ele é \033[0:34mescaleno')
else:
    print('\033[0:31mNão é possível formar um triangulo.\033[m')