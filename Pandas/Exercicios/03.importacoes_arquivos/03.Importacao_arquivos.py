# %%
import pandas as pd

df = pd.read_csv("../dataset_pandas/clientes.csv", sep = ';')

# %%
'Salva o arquivo no diretório que está trabalhando'
df.to_csv("clientes.csv", index = False)
# %%

df.to_parquet("clientes.parquet", index = False)

df2 = pd.read_parquet("clientes.parquet")
# %%
df.to_excel("clientes.xlsx", index = False)
df3 = pd.read_excel("clientes.xlsx")
# %%
'Lê o que está no CTLR C. Utilizado para trabalhos rápidos de análise/teste'
df4 = pd.read_clipboard()
df4.to_csv("UF.csv",sep=';')

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
df5 = pd.read_html(url)

# %%
