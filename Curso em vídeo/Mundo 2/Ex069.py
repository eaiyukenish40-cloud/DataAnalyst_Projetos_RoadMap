#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas têm mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres têm menos de 20 anos.
homens = mulheres = maior_idade = cadastro = 0
while True:
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    cadastro += 1
    if idade >= 18:
        maior_idade = maior_idade + 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = int(input('Deseja continuar?\n[1].Sim\n[2].Não\n'))
    if opcao == 2:
        print(f'Temos {maior_idade} pessoas com mais de 18 anos. {homens} homens cadastrados. E {mulheres} mulheres com menos de 20 anos. E {cadastro} cadastrados.')
        break
