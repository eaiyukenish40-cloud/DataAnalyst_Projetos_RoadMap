#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(a):
    #print(f'Entrou no leia int a = {a}')
    tipo = 'inteiro'
    v = trataerro(tipo,str(a))
    #print(f'O valor {v} é {tipo}.')
    return v

def leiafloat(a):
    tipo = 'real'
    v = trataerro(tipo,str(a))
    #print(f'O valor {v} é {tipo}.')

def trataerro(tipo,a):
    try:
        while True:
            if tipo == 'inteiro':
                if a == 'Digite um número inteiro: ':#programa 113
                    msg = int(input(a))
                else:
                    msg = int(a)
                return msg
            else:
                msg = str(input(a)).replace(',','.').strip()
                return float(msg)
    except KeyboardInterrupt:
        print('\033[0:33mPrograma interrompido pelo usuário. Não foi digitado um valor.\033[m')
        return 0
    except:
        #print(f'Entrou no except do trataerro.')
        print(f'\033[0:31mVocê não digitou um número {tipo} válido.\033[m')
        while True:
            msg = str(input('Digite novamente: '))
            if msg.isnumeric() and tipo == 'inteiro':
                return int(msg)
            if tipo == 'real':
                if msg.isalpha() or msg == '':
                    print(f'\033[0:31mVocê não digitou um número {tipo} válido.\033[m')
                else:
                    return float(msg.replace(',','.'))
            else:
                print(f'\033[0:31mVocê não digitou um número {tipo} válido.\033[m')
    else:
        while True:
            msg = int(input(a))
            return msg
    finally:
        print(f'\033[0:32mOpção válida. Programa de validação do tipo "{tipo}" encerrado.\033[m')