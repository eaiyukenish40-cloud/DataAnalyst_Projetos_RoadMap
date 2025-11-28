#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.

comparador = 0
count_ref = 0
count_m = 0
soma = 0
homem_Velho = ''
mulheres = []
for c in range(0,4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: \n[1.]Masculino\n[2.]Feminino:\n '))
    soma = soma + idade
    if count_ref == 0 and sexo == '1':
        count_ref = count_ref + 1
        comparador = idade
        homem_Velho = nome
        #print(comparador,homem_Velho)
    if sexo == '1':
        if idade > comparador:
            comparador = idade
            homem_Velho = nome
            #print('mais velho ',comparador, homem_Velho)
    else:
        if idade < 20:
            count_m = count_m +1
            mulheres.append(nome)
            #print('Mulheres ',nome )
media = soma / 4
print('A média de idade do grupo é \033[0:32m{:.2f}\033[m.\nO homem mais velho é o \033[0:32m{}\033[m com {}.\nO número de mulheres menor de 20 anos são \033[0:33m{}\033[m: \033[0:32m{}\033[m'.format(media,homem_Velho,comparador,count_m,mulheres))
