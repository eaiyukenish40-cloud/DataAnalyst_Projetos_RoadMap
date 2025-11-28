#Aprimore o DESAFIO 093 (Gerenciamento de Aproveitamento de Jogador de Futebol) para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
lista = []
soma = 0
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().lower().capitalize()
    partidas = int(input('Quantas partidas jogou? '))
    for c in range(0, partidas):
        jogador[f'partida {c+1}'] = int(input(f'Quantos gols na partida {c+1}? '))
        soma += jogador[f'partida {c+1}']
    jogador['Saldo total gols'] = soma
    lista.append(jogador.copy())
    jogador.clear()
    print(lista)
    jogador['Saldo total gols'] = soma
    desejo = str(input('Dejesa continuar?[S/N]: ')).strip().upper()[0]
    soma = 0
    if desejo == 'N':
        break
for c,v in enumerate(lista):
    print(f'Jogador: N°{c+1:<10} Nome: {v["nome"]:<10} Saldo de gols:{v["Saldo total gols"]}')

while True:
    n = int(input('Mostrar detalhes de qual jogador? '))
    print(f'Jogador: N°{n}, {lista[n-1]["nome"]}, teve o seguinte desempenho: ')
    for c, v in lista[n-1].items():
        if c != 'nome' and c != 'Saldo total gols':
            print(f'{c}: {v} gol(s)')
