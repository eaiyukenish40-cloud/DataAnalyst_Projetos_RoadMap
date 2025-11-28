#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
def aumentar(a, aum = 0):
    """
    :param a: Valor a ser aumentado
    :param aum: Valor percentual de aumento
    :return: Retorna o valor a ser aumentado
    """
    a = a*(1 + aum/100)
    return a
def diminuir(d, dim = 0):
    """
    :param d: Valor a ser diminuido
    :param dim: Percentual de diminuição
    :return: Retorna o valor a ser diminuido
    """
    d = d*(1 - dim/100)
    return d
def dobro(dd):
    """
    :param dd: Valor a ser dobrado
    :return: Retorna o valor dobrado
    """
    dd = dd * 2
    return dd
def metade(m):
    """
    :param m: Valor a ser metade
    :return: Retorna a metade
    """
    m = m/2
    return m
def moeda(valor, formato = 'N'):
    if formato == 'S':
        valor = f'R$ {valor:.2f}'.replace('.',',')
    return valor

def resumo(n, p = 0, dim = 0):
    """
    Função que trás um resumo financeiro do valor inputado.

    :param n: Valor a ser aumentado
    :param p: Porcentagem de aumento
    :param dim: Porcentagem de queda
    """
    a = aumentar(n, p)
    d = diminuir(n, dim)
    dd = dobro(n)
    m = metade(n)
    print('-'*len('RESUMO DO VALOR'))
    print('RESUMO DO VALOR')
    print('-' * len('RESUMO DO VALOR'))
    print(f'Preço analisado: \t{moeda(n,'S'):>5}')
    print(f'Dobro do preço: \t{moeda(dd,'S'):>5}')
    print(f'Metade do preço: \t{moeda(m,'S'):>5}')
    print(f'Aumento de {p}%: \t{moeda(a,'S'):>5}')
    print(f'Queda de {dim}%: \t{moeda(d,'S'):>5}')
    print('-' * len('RESUMO DO VALOR'))