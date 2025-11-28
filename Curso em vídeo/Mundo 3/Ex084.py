# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
pessoas = []
cadastro = []
peso_maior = []
peso_menor = []
maior = menor = 0
while True:
    nome = str(input("Digite o seu nome: ")).strip().lower().capitalize()
    peso = int(input("Digite o seu peso: "))
    pessoas.append(nome)
    pessoas.append(peso)
    cadastro.append(pessoas[:])
    pessoas.clear()
    continuar = ''
    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(cadastro)
for c, v in enumerate(cadastro): #pega o maior peso
    if c == 0:
        maior = v[1]
        menor = v[1]
    if v[1] > maior:
        maior = v[1]
    elif v[1] < menor:
        menor = v[1]
for c,v in enumerate(cadastro):
    if v[1] == maior: #pega o nome da pessoa de maior peso
        peso_maior.append(v[0])
    if v[1] == menor: #pega o nome da pessoa de menor peso
        peso_menor.append(v[0])
print(f"O número de pessoas cadastradas foi {len(cadastro)}",end = '.')
print(f'As pessoas mais pesadas são: \033[0:33m{peso_maior}\033[m com \033[0:33m{maior}\033[m KG. E menor peso: \033[0:31m{peso_menor}\033[m com \033[0:31m{menor}\033[m KG.')
