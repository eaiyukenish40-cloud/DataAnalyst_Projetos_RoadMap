#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.
pessoa = {}
mulheres = []
lista = []
maiormed = []
media = soma = 0
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().lower().capitalize()
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    desejo = str(input('Dejesa continuar?[S/N]: ')).strip().upper()[0]
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    if desejo == 'N':
        break

media = soma / len(lista)
print(f'A quantidade de pessoas cadastradas foi: \033[0:33m{len(lista)}\033[m')
print(f'A média de idade do grupo é \033[0:32m{media:.2f}\033[m anos')
for k, v in enumerate(lista):
    for a,b in v.items():
        if a == 'Sexo' and b == 'F':
            mulheres.append(v['Nome'])
        if a == 'Idade' and b > media:
            maiormed.append(v.copy())
print(f'As mulheres são: {mulheres}')
print(f'As pessoas com idade acima da média {media} são: {maiormed}')
