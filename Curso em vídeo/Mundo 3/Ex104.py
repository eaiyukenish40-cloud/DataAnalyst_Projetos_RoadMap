#Crie um programa que tenha a Função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')
def leiaint(a):
    print(a,end='')
    while True:
        msg = input()
        if msg.isnumeric():
            return msg
        else:
            print(f'\033[0:31mVocê digitou letras.Digite apenas números inteiros.\033[m')




n = leiaint('Digite um número: ')
print(f'Você digitou o número: {n}')