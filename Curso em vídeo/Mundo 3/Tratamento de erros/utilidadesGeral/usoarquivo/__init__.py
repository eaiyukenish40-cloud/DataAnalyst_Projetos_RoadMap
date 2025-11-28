def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('\033[0:31mArquivo procurado não encontrado\033[m')
    else:
        return True

def criarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as e:
        print(f'Erro na criação {e.__cause__}')
    else:
        print(f'Arquivo \033[0:32m{nome}\033[m criado com sucesso')

def lerarquivo(nome):
    temp = []
    try:
        a = open(nome, 'rt')
    except:
        print('\033[0:31mErro ao ler o arquivo\033[m')
    else:
        print('-'*30)
        print(f'{"Pessoas cadastradas":^30}')
        for i in a:
            temp = i.split(';')
            print(f'\033[35m{temp[0]:<27}\033[m{temp[1]:>3}', end='')
        print(f'{a.read()}')
        print('-' * 30)

def cadastropess(arq, pessoa ='desconhecido', idade = 'desconhecido'):
    try:
        a = open(arq, 'at')
    except Exception as e:
        print(f'\033[0:31mErro ao abrir o arquivo\033[m {e.__class__}')
    else:
        try:
            a.write(f'{pessoa};{idade}\n')
        except Exception as e:
            print(f'\033[0:31mErro ao abrir o arquivo\033[m {e.__class__}')
        else:
            print(f'\033[0:32mPessoa registrada com sucesso\033[m')
