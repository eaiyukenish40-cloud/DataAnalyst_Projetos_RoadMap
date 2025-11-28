'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas.

O nome com todas as letras minúsculas.

Quantas letras ao todo (sem considerar espaços).

Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('O nome {} tem {} letras'.format(nome, len(nome) - nome.count(' ')))
print(len(nome.replace(' ', '')))
print(len(nome)-nome.count(' '))
print(len(nome.split()[0]))