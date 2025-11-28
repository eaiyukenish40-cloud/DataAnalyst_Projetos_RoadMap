#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# Saída: ~~~~~~~~~~~~~ Olá, Mundo! ~~~~~~~~~~~~~
def escreva(txt):
    tam = len(txt)
    print('-'*tam)
    print(f'{txt}')
    print('-' * tam)

escreva(str(input('Digite algo: ')).strip())