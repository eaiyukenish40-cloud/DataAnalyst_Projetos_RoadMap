def leiaDinheiro(msg):
    n = str(input(msg)).strip() # obs era possível colocar o .replace(',','.') na própria entrada de dados
    letra = n.isalpha()
    while True:
        if n != '' and letra == False:
            virg = n.find(',') # desnecessário colocando o replace no início.
            if virg != -1:
                n = float(n.replace(',', '.'))
                return n
            else:
                n = float(n)
                return n
        else:
            while n == '' or n.isalpha():
                n = str(input('Você não digitou corretamente. Tente novamente: ')).strip()
            letra = False

def leiaint(a):
    print(a,end='')
    while True:
        msg = input()
        if msg.isalpha():
            print(f'\033[0:31mVocê digitou letras.Digite apenas números inteiros.\033[m')
        else:
            return msg