'''
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".

Em que posição ela aparece a primeira vez.

Em que posição ela aparece a última vez.'''
frase = input('Digite uma frase: ').strip()
print(frase.upper().count('A'))
print(frase.upper().find('A')+1)
print(frase.upper().rfind('A')+1)
print(frase.upper().strip())