# %%

import pandas as pd

df_clientes = pd.read_csv("../dataset_pandas/clientes.csv", sep = ';')
# %%
"representa as primeiras linhas do dataframe"
df_clientes.head(n=10)
# %%
"representa as ultimas linhas do dataframe"
df_clientes.tail(n=10)
# %%
'representa uma amostra aleatória do dataframe'
df_clientes.sample()
# %%
'representa o número de linhas e colunas do dataframe'
df_clientes.shape
# %%
'representa os nomes das colunas do dataframe'
df_clientes.columns
# %%
'representa os índices do dataframe'
df_clientes.index
# %%
'representa o tipo de dados de cada coluna do dataframe'
df_clientes.info(memory_usage='deep')
df_clientes.info()
# %%
'representa o tipo de dados de cada coluna do dataframe'
type(df_clientes.dtypes)
# %%
df_transacoes = pd.read_csv("../dataset_pandas/transacoes.csv", sep = ';')

# %%
df = df_clientes.rename(columns={'id_cliente': 'id'})
# %%
"Equivalente SQL no Pandas"
# SELECT * FROM df_clientes
df_clientes

# SELECT idCliente,qtPontos FROM df_clientes
"A ordem que for colocada na coluna, é a ordem que vai aparecer no resultado"
df_clientes[['id_cliente', 'qt_pontos']]

"Ordenar colunas em ordem alfabética"
colunas = df_clientes.columns.tolist() #transforma o index das colunas do DF em uma lista
colunas.sort() #reodernada a lista em ordem alfabética