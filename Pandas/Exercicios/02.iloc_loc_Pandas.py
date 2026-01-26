# %%
import pandas as pd
idades = [32, 38, 30, 30, 31, 35, 25, 29, 31, 37, 27, 23, 36, 33, 32]
series_idades = pd.Series(idades)
print(f"A média das idades é: {series_idades.var()}")

series_idades = pd.Series(idades, index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"])

dicio = {'a': 32, 'b': 38, 'c': 30, 'd': 30, 'e': 31, 'f': 35, 'g': 25, 'h': 29, 'i': 31, 'j': 37, 'k': 27, 'l': 23, 'm': 36, 'n': 33, 'o': 32}

# crie uma lista com varios nomes de pessoas, considere 15 nomes
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Hugo', 'Isabela', 'João', 'Karina', 'Lucas', 'Mariana', 'Nicolas', 'Olivia']
series_nomes = pd.Series(nomes)
df = pd.DataFrame()
df["nomes"] = series_nomes
# %%
df["idades"] = pd.Series(idades)

# %%
df.iloc[1]
# %%
series_idades['a']
# %%
