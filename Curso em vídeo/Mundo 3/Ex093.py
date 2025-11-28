#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
soma = 0
jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().lower().capitalize()
partidas = int(input('Quantas partidas jogou? '))
for c in range(0, partidas):
    jogador[f'partida {c+1}'] = int(input(f'Quantos gols na partida {c+1}? '))
    soma += jogador[f'partida {c+1}']
jogador['Saldo total gols'] = soma
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas. E fez um total de {jogador["Saldo total gols"]} gols.')