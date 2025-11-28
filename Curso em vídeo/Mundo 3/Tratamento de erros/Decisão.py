def prosseguir(n):
    while n != 'N':
        n = str(input('Deseja continuar?:[S/N] ')).strip().upper()[0]
        if n != 'S' and n != 'N':
            n = str(input('\033[0:31mOpção inexistente.\033[mDeseja continuar?:[S/N] ')).strip().upper()[0]
        elif n == 'S':
            return n
            break

def escolha3(n):
    from utilidadesGeral import entradaDados
    #print(f'Entrou no decisão n = {n}')
    n = entradaDados.leiaint(n)
    while n > 3 or n < 0 :
        n = int(input('\033[0:31mOpção inexistente.\033[mDigite sua opção: '))
    return n
