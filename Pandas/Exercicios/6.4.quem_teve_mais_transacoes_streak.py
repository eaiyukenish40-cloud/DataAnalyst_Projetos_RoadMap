# %%
#06.04 - Quem teve mais transações de Streak?
import pandas as pd

produtos = pd.read_csv('../dataset_pandas/produtos.csv',sep=';')
transacaoProduto = pd.read_csv('../dataset_pandas/transacao_Produto.csv',sep=';')
transacoes = pd.read_csv('../dataset_pandas/transacoes.csv',sep=';')
# %%
"merge entre transacao e transacaoProduto para obter o IdProduto e depois merge com produtos para obter o nome do produto"
join_1 = transacoes.merge(transacaoProduto, left_on='IdTransacao', right_on='IdTransacao', how='left', suffixes=('_transacao', '_transacaoProduto'))[['IdTransacao', 'IdProduto','IdCliente']]

# %%
"merge final com as 3 tabelas transacao, transacaoProduto e produtos por meio do IdProduto"
join_2 = join_1.merge(produtos, left_on='IdProduto', right_on='IdProduto', how='left', suffixes=('_join1', '_produto'))
# %%
filtro = join_2['DescNomeProduto'] == 'Presença Streak'
# %%

contagem_streak = join_2[filtro].groupby('IdCliente', as_index=False).agg(
    {'IdTransacao':'count'}).sort_values(by='IdTransacao', ascending=False)

contagem_streak.columns = ['IdCliente', 'QtdeTransacoesStreak']
# %%
"ou"
join_2[filtro].groupby('IdCliente')['IdTransacao'].count().sort_values(ascending=False).head(1)
# %%
