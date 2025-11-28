#Faça um programa que tenha uma Função chamada Ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = '', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0

    print(f'O jogador {nome} fez {gols} gols.')


ficha(str(input('Digite o nome do jogador: ')).strip().lower().capitalize(),str(input('Digite a quantidade de gols: ')))