# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.
def ajuda(msg):
    while True:
        tam = len(msg)
        print('\033[0:30:42m-\033[m'*tam)
        print(f'\033[0;30:42m{msg}\033[m')
        print('\033[0:30:42m-\033[m'*tam)
        funcao = str(input('Função ou biblioteca: ')).strip().lower()
        if funcao == 'fim':
            break
        print('\033[7:30m')
        help(funcao)
        print('\033[m')


ajuda('Sistema de ajuda HelPython')