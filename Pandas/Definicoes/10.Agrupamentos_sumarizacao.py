# %%

import pandas as pd

clientes = pd.read_csv('../dataset_pandas/clientes.csv', sep=';' )

"sumarização de dados"
clientes["flTwitch"].sum()
clientes["flTwitch"].mean()
# %%
"aplicação de cálculos em múltiplas colunas"
redes = ["flEmail", "flInstagram", "flTwitch", "flBlueSky","flYouTube"]
clientes[redes].describe()

# %%
"retorna uma série com as informações do dataframe tipos primitivos de cada coluna"
clientes.dtypes

"filtro"
filtro_tipo_coluna = clientes.dtypes == 'object'
clientes.dtypes[~filtro_tipo_coluna] #~ é a negação do filtro
index = clientes.dtypes[~filtro_tipo_coluna].index.tolist()
# %%
"AGRUPAMENTOS"

transacoes = pd.read_csv('../dataset_pandas/transacoes.csv', sep=';')

transacoes.groupby(by=["IdCliente"], as_index=False)[['IdTransacao']].count()#conta o número de transações por cliente. O as_index=False é para manter o IdCliente como uma coluna normal, em vez de transformá-lo em um índice. O [['IdTransacao']] é para selecionar apenas a coluna IdTransacao para contar.

# %%

sumary = transacoes.groupby(by=["IdCliente"], as_index=False).agg(
    {'IdTransacao':['count'],                                                      
    'QtdePontos':['sum','mean']}) #conta o número de transações e soma
# %%

sumary.columns = ['IdCliente', 'QtdeTransacoes', 'TotalPontos', 'MediaPontos'] #renomeia as colunas do dataframe sumary
# %%

"criando funções personalizadas para o groupby"

def modulo_diff_amplitude(x: pd.Series):
    import numpy as np
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2) 


def life_time(x: pd.Series):
    data = pd.to_datetime(x)
    return (data.max() - data.min()).days

idade = pd.Series([25, 30, 22, 35, 28, 40, 23, 31, 29, 27])

modulo_diff_amplitude(idade)

resultado = transacoes.groupby(by=["IdCliente"], as_index=False).agg({
    'IdTransacao':['count'],
    'QtdePontos':['sum','mean', modulo_diff_amplitude],
    'DtCriacao':[life_time]
})
resultado.columns = ['IdCliente', 'QtdeTransacoes', 'TotalPontos', 'MediaPontos', 'ModDiffAmplitudePontos', 'Tempo de duração']
# %%

