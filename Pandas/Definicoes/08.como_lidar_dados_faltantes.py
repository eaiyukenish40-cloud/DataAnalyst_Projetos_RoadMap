# %%

import pandas as pd

teste = {
    "nome": ["Téo", None, "Nah", "Marcio"],
    "idade": [None, None, 43, 52],
    "salario": [3453, 4324, None, 5423]
}

df = pd.DataFrame(teste)
# %%
df.dropna()  # dropna() remove as linhas que possuem dados faltantes. Não modifica o DF original.
df.dropna(how = 'all')  #dropna(how = 'all') remove as linhas que possuem todos os dados faltantes. Não modifica o DF original.

df.dropna(how = 'any')  #dropna(how = 'any') remove as linhas que possuem qualquer dado faltante. Não modifica o DF original.

# %%
df.dropna(how ="all", subset = ['idade']) #retira o NA somente da coluna idade como critério de remoção de linha. subset defini o critério de remoção de linha, ou seja, somente as linhas que tiverem NA na coluna idade serão removidas. Não modifica o DF original.

# %%
df.fillna(0)  #fillna() preenche os dados faltantes com um valor específico. No caso, preenche os dados faltantes com 0. Não modifica o DF original.
# %%
df["idade"].fillna(df["idade"].mean())  #fillna() preenche os dados faltantes com um valor específico. No caso, preenche os dados faltantes da coluna idade com a média da coluna idade. Não modifica o DF original.