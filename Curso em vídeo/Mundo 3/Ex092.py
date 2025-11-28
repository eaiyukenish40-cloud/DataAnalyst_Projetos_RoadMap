#Crie um programa que leia nome, ano de nascimento e carteira de trabalho (CTPS) e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
pessoa = {}
from datetime import date
today = date.today().year

pessoa['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
pessoa['Idade'] = today - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o seu salário: '))
    pessoa['Aposentadoria anos'] = 35 - (today - pessoa['Ano contratação']) + pessoa['Idade']
for k, v in pessoa.items():
    print(f'O {k}: {v}')