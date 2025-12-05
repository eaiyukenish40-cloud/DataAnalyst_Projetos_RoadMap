# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from modulos_sistemas import cadastro_design,dados_manipul
from time import sleep
from datetime import date
print('-' * 40)
print(f'{'Seja bem vindo ao sistema de cadastro':^40}')
print('-' * 40)
print(f'\033[0:33mCarregando...\033[m')
sleep(1)
while True:
    #chama a função do pacote importado. Onde é gerado o layout do mnu de operação. Retorna uma valor inteiro para ser utilizado na sequencia do programa
    n = cadastro_design.header_conf('Menu Principal')
    # inicio do tratamento de erros.
    try:
        #Usuário insere o nome do arquivo a ser lido.
        nome = str(input('Digite o nome do arquivo a ser lido: '))
    except KeyboardInterrupt:
        # interrompe o programa
        print('\033[0:31mVocê desejou sair do programa\033[m')
        raise
    except:
        print('\033[0:33mHouve um problema ao continuar. Tente novamente.\033[m')
        continue
    else:
        #chama a função de verificação do arquivo.
        if n == 1:
            status = dados_manipul.arq_existe(nome)
            # se não existe o arquivo selecionado, é dado a opção de ser criado
            if status is False:
                while True:
                    try:
                        o = int(input('Deseja criar arquivo?\n[1].Sim\n[2].Não '))
                    except KeyboardInterrupt:
                        raise print('\033[0:31mVocê desejou sair do programa\033[m')
                    except (ValueError,TypeError):
                        print('\033[0:31mOpção incorreta tente novamente\033[m.')
                        continue
                    else:
                        if o == 1:
                            dados_manipul.criar_arquivo(nome)
                        else:
                            break
            else:
                #chama a função de leitura do arquivo.
                dados_manipul.lerArquivo(nome)
        #cadastra a nova pessoa
        elif n == 2:
            pessoa = str(input('Digite o nome da pessoa a ser cadastrada: '))
            idade = date.today().year - int(input('Ano de nascimento: '))
            print(idade)
            dados_manipul.cadastro(nome, pessoa, idade)
        elif n == 3:
            print('\033[0:33mSaindo do programa...\033[m')
            break
        else:
            print('Opção invalida. Tente novamente.')

