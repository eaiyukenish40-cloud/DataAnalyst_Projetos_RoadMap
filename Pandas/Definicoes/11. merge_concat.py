
# %%

import pandas as pd
transacoes = pd.read_csv("../dataset_pandas/Transacoes.csv", sep=";")
clientes = pd.read_csv("../dataset_pandas/Clientes.csv", sep=";")   

transacoes.rename(columns={"idCliente": "IdCliente"}, inplace=True)
# %%
"join pelo pandas colunas com o mesmo nome"
join_cliente_transacoes = transacoes.merge(right=clientes, how='left', on=['idCliente'],suffixes=['_transacao', '_cliente'])
# %%

"join com colunas nomes diferentes"
join_cliente_transacoes2 = transacoes.merge(right=clientes, left_on='IdCliente',right_on='idCliente', how='left', suffixes=['_transacao', '_cliente'])

# %%
' trabalho com concat'
df = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5],
    "nome": ["teo", "jose", "nah", "mah", "lah"]
})

df2 = pd.DataFrame({
    "cliente": [6, 7, 8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32, 29, 31]
})

pd.concat([df,df2], ignore_index=True)
# %%

df3 = pd.DataFrame({
    'idade': [32, 29, 31, 12, 10]
})

df3.sort_values(by='idade',inplace=True)
df3.reset_index(drop=True, inplace=True)

concat = pd.concat([df, df3], axis=1)
# %%

df = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
    'estado': ['SP', 'RJ', 'MG','ES','SC']
})

df2 = pd.DataFrame({
    "cliente": [6, 7, 8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32, 29, 31],
    'estado': ['SP', 'RJ', 'MG']
})
df.set_index(['estado'], inplace=True)
df2.set_index(['estado'], inplace=True)
concat2 = pd.concat([df, df2], axis=1, ignore_index=True)
# %%
