#selecione a primeira transacao diária

# %%
import pandas as pd

transacoes = pd.read_csv('../dataset_pandas/transacoes.csv',sep=';')
# %%

transacoes = transacoes.sort_values(by='DtCriacao', ascending=True)
# %%
transacoes['Data'] = pd.to_datetime(transacoes['DtCriacao']).dt.date
# %%
transacoes.drop_duplicates(subset=['Data'], keep='first')
# %%
