def prosseguir(n):
    while n != 'N':
        n = str(input('Deseja continuar?:[S/N] ')).strip().upper()[0]
        if n != 'S' and n != 'N':
            n = str(input('\033[0:31mOpção inexistente.\033[mDeseja continuar?:[S/N] ')).strip().upper()[0]
        elif n == 'S':
            return n
            break