import pandas as pd


def varianca(valores: list) -> float:
    """_summary_

    Args:
        idades (list): repassado uma lista de valores

    Returns:
        float: _description_
    """
    media = sum(valores) / len(valores)
    dif = 0
    for valor in valores:
        dif += (valor - media) ** 2
    return dif / (len(valores) - 1), media


# crie uma lista com várias idades aleatorias, considere mais de 40 idades
idades = [32, 38, 30, 30, 31, 35, 25, 29, 31, 37, 27, 23, 36, 33, 32]

'''media = varianca(idades)[1]
print(f"A média das idades é: {media}")

resultado = varianca(idades)[0]
print(f"A variância das idades é: {resultado}")'''


#Usando pd.Series - acesso a médotodos de estatística:
idades = [32, 38, 30, 30, 31, 35, 25, 29, 31, 37, 27, 23, 36, 33, 32]
series_idades = pd.Series(idades)
print(f"A média das idades é: {series_idades.var()}")
series_idades.sort_values()

