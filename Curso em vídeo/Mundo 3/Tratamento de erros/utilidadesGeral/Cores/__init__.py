def cor(tipo = 'Nenhuma'):
    """

    :param tipo: escolha de qual cor desejada
    :return: retonar a cor
    """
    tipo = tipo.strip().lower().capitalize()
    cores = {'Amarelo':'\033[0:33m','Verde':'\033[0:32m','Vermelho':'\033[0:31m','Nenhuma':'\033[m'}
    return cores[tipo]