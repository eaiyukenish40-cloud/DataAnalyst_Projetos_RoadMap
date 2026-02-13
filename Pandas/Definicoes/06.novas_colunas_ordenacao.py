# %%
import pandas as pd

df = pd.read_csv('../dataset_pandas/clientes.csv', sep=';' )


# %%
"para somar valores nas linhas de uma coluna, basta fazer operações escalares"
df['qtdePontos'] + 100

"criar uma nova coluna"

df['qtdePontos_100'] = df['qtdePontos'] + 100
# %%
"visualização estatística da nova coluna"
df['qtdePontos_100'].describe()

# %%
"ordenar os valores da nova coluna"
df['qtdePontos_100'].sort_values(ascending=False).head(5)
# %%

dicionario_pessoas = {
  "nome": ["teo", "ana", "nah", "jose"],
  "idade": [32, 43, 35, 42],
  "salario": [2345, 4533, 3245, 4533]
}
df = pd.DataFrame(dicionario_pessoas)
df.sort_values(by=['salario','idade'], ascending=[True,False])
# %%
