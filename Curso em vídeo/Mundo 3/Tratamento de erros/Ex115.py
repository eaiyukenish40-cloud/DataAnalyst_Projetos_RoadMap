# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from utilidadesGeral import Cores,entradaDados
from utilidadesGeral import usoarquivo
import Decisão
from time import sleep
c = 0
try:

    while True:
        print('-'*30)
        print(f'{'Menu principal':^30}')
        print('-'*30)
        print(f'{Cores.cor('Amarelo')}1{Cores.cor('Nenhuma')} - {Cores.cor('verde')}Ver pessoas cadastradas{Cores.cor('nenhuma')}')
        print(f'{Cores.cor('Amarelo')}2{Cores.cor('Nenhuma')} - {Cores.cor('verde')}Cadastrar nova Pessoa{Cores.cor('nenhuma')}')
        print(f'{Cores.cor('Amarelo')}3{Cores.cor('Nenhuma')} - {Cores.cor('verde')}Sair do Sistema{Cores.cor('nenhuma')}')
        print('-'*30)
        n = Decisão.escolha3(str(input('Digite sua opção: ')))
        if c == 0:
            nome = str(input('Digite seu nome do arquivo para conferir: ')).strip().lower()
            if not usoarquivo.arquivoexiste(nome):
                print(f'Não existe: {usoarquivo.arquivoexiste(nome)}')
                usoarquivo.criarquivo(nome)
            c = 1
        if n == 1:
            usoarquivo.lerarquivo(nome)
            sleep(1)

        elif n == 2:
            pessoa = str(input('Digite o nome da pessoa ser cadastrada: ')).strip().lower().capitalize()
            idade = int(input('Digite sua idade: '))
            usoarquivo.cadastropess(nome,pessoa,idade)
            sleep(1)


        else:
            c = 0
            print(f'{Cores.cor("amarelo")}Programa finalizado{Cores.cor("nenhuma")}')
            break
except:
    print('Programa encerrado.')
    #n = Decisão.escolha3(str(input('Digite sua opção: ')))
