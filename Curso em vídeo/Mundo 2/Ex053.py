#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA
palavra = str(input('Digite uma frase: ')).strip().upper()
palavras = palavra.replace(' ','')
size = len(palavras)
count = 0
for c in range(0,len(palavras)):
    if palavras [c] == palavras[size - c-1]:
        count = count + 1
if count == size:
    print('\033[0:33m{}\033[m É um palindromo'.format(palavra.lower().capitalize()))
else:
    print('\033[0:33m{}\033[m não é um palindromo'.format(palavra.lower().capitalize()))
