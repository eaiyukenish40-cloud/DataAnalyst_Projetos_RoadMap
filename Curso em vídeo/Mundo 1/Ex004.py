'💡 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'
teste = input('Digite algum caractere: ')
print('O caractere digitado é um {}'.format(type(teste)))
'verifica qual outro tipo pode ser'
print('é um número?',teste.isnumeric())
print('é um alpha?',teste.isalpha())
print('é um alphanúmero?',teste.isalnum())
print('é um tem espaço?',teste.isspace())
print('é maiusculo?',teste.isupper())