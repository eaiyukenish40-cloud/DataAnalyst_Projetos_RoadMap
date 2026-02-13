# %%
import pandas as pd

df = pd.read_csv("../dataset_pandas/transacoes.csv", sep = ';')
df.head()


# %%

#Demonstração de filtros utilizando listas e dicionários
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# filtra apenas os valores pares da lista
pares = [i for i in lista if i % 2 == 0]

dicionario = {
  "nome": ["teo", "nah", "mah"],
  "idade": [32, 35, 14],
  "uf": ["sp", "pr", "rj"]
}

# %%
teste = pd.DataFrame(dicionario)

filtro = teste["idade"] > 15
filtro = filtro.tolist()

teste[filtro]
# %%
"AND = conseguir filtrar a quantidade de pontos maior ou igual a 50 e menor que 100"
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)

# %%
"OR = conseguir filtrar a quantidade de pontos  igual a 5 OU menor que 100"
filtro = (df["QtdePontos"] == 5) | (df["QtdePontos"] < 100)
# %%

# metodos operadores nos filtros
df = pd.read_csv("../dataset_pandas/produtos.csv", sep = ';')

filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 1)
# é equivalente a:
filtro = df["IdProduto"].isin([1, 5])
# %%
"Instanciação de novos dataframes a partir de filtros. O comportamento é o mesmo de uma lista. Ambas estão instanciadas no mesmo lugar de memória, ou seja, se eu alterar um valor em um dos dataframes, o outro também será alterado. Para evitar isso, é necessário criar uma cópia do dataframe utilizando o método copy()"

df1 = pd.read_csv("../dataset_pandas/clientes.csv", sep = ';')
filtro = df1["flEmail"] == 1
resultado = df1[filtro]
# %%
resultado["teste"] = 1
