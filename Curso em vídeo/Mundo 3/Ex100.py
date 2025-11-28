#Faça um programa que tenha uma lista chamada números e duas Funções chamadas sorteia() e somaPar().
# A primeira Função vai sortear 5 números e vai colocá-los dentro da lista e a segunda Função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
def somaPar(sum):
    soma = 0

    for i,c in enumerate(sum):
        print(c)
        if c % 2 == 0:
            soma += c
    print(f'A soma entre os valores pares da lista sorteada, é \033[0:33m{soma}\033[m')
def sorteia(lst):
    global lista
    lista = [randint(1,100), randint(1,100), randint(1,100), randint(1,100),randint(1,100)]
    somaPar(lst)

## começo do programa
lista = []
sorteia(lista)
print(f'Lista sorteada: {lista}')


