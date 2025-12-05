def header_conf(a=''):
    from time import sleep
    tam = len(a)
    print('-'*40)
    print(f'{'Seja bem vindo ao sistema de cadastro':^40}')
    print('-' * 40)
    print(f'\033[0:33mCarregando...\033[m')
    sleep(1)
    print('-'*40)
    print(f'{a:^40}')
    print('-' * 40)
    system('Menu')


def system(b=''):
    if b == 'Menu':
        print(f'\033[0:33m1\033[m - \033[0:32mVer pessoas cadastradas\033[m')
        print(f'\033[0:33m2\033[m - \033[0:32mCadastrar nova Pessoa\033[m')
        print(f'\033[0:33m3\033[m - \033[0:32mSair do Sistema\033[m')
        print('-' * 40)
        try:
            n = int(input('Digite sua opção: '))
        except KeyboardInterrupt:
            print('\033[0:31mVocê desejou sair do programa\033[m')
        except Exception as ex:
            print(f'\033[0:31mErro: {ex}\033[m')
        else:
            return n