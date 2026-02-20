# %%

import pandas as pd
import os

lista_arquivos = os.listdir('../IPEA')  #retorna uma lista com os arquivos do diretório

#ELT dos arquivos do IPEA alterando o nome da coluna valor conforme o arquivo e setando o index para nome e período, comum a todos os arquivos.
def read_file(file_name:str):
    arquivo = pd.read_csv(f'../IPEA/{file_name}.csv', sep=';')
    arquivo = arquivo.rename(columns={'valor':file_name})
    arquivo.set_index(["nome","período"], inplace=True)
    arquivo.drop(['cod'], axis=1, inplace=True)
    return arquivo

#Criando uma lista de dataframes a partir da lista de arquivos do diretório, utilizando a função read_file para ler cada arquivo e processá-lo.
dfs = []
for i in lista_arquivos:
    lista_arquivos = i.split('.')[0]
    dfs.append(read_file(lista_arquivos))

#A junção em uma única view ocorre por meio do concat, utilizando o index comum a todos os dataframes, nome e período.

tabela_final = pd.concat(dfs, axis=1)
tabela_final.head()

# %%

tabela_final.to_csv('../IPEA/tabela_final.csv', sep=';')

# %%

"Abaixo, o EDA dos arquivos do IPEA. Antes da construção da função read_file, para entender a estrutura dos arquivos e o processo de ETL necessário para a construção da função."
homicidios_geral = pd.read_csv('../IPEA/homicidios.csv', sep=';')

homicidios_geral.rename(columns={'valor': 'homicidio_geral'}, inplace=True)
homicidios_geral.drop(['cod'], axis=1, inplace=True)
homicidios_geral.head()

# %%
homicidios_negros = pd.read_csv('../IPEA/homicidios-negros.csv',sep=';')
homicidios_negros.head()
homicidios_negros.rename(columns={'valor': 'homicidio_negros'}, inplace=True)

# %%
homicidios_jovens_armas = pd.read_csv('../IPEA/homicidio-de-jovens-por-armas-de-fogo.csv', sep=';')

homicidios_jovens_armas.rename(columns={'valor': 'homicidio_jovens_armas'}, inplace=True)
homicidios_jovens_armas.head()

# %%

homicidios_geral.set_index(['nome','período'], inplace=True)
homicidios_negros.set_index(['nome','período'], inplace=True)
homicidios_jovens_armas.set_index(['nome','período'], inplace=True)


# %%

df =pd.concat([homicidios_geral, homicidios_negros, homicidios_jovens_armas], axis=1)