# %%
import pandas as pd

df = pd.read_csv("../SQL - Curso Teo_me_why/produtos.csv", sep=';')
df.to_csv("produtos.csv",index=False)
# %%
