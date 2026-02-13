# %%

import pandas as pd

df = pd.read_csv("../dataset_pandas/clientes.csv", sep=";")


# %%
"conversão de tipos nas colunas"
df["qtdePontos"].astype(str).astype(int)
df["qtdePontos"].astype(float)

resultado = df["qtdePontos"] + 100
# %%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
# %%
df["DtCriacao"].dt.month.astype(int)
# %%
