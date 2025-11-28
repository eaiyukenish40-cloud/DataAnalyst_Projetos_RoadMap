'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria da Souza
primeiro = Ana
último = Souza'''
nome = input('Digite o nome de uma pessoa: ').strip()
print(nome.split()[0],'\n',nome.lstrip().split()[len(nome.split())-1])