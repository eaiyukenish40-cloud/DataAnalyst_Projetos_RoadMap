def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        print('\033[0:31mErro. Arquivo não existe\033[m')
        return False
    except KeyboardInterrupt:
        print('\033[0:31mVocê desejou sair do programa\033[m')
        raise
    except:
        print('\033[0:31mHouve um erro ao tentar abrir o arquivo\033[m')
    else:
        print('\033[0:32mArquivo existe\033[m')

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[0:31mErro ao criar o arquivo\033[m')
    else:
        print('\033[0:32mArquivo criado com sucesso\033[m')