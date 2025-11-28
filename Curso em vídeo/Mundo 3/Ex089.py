# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
informaçoes = []
média = 0
count = 0
while True:
    count += 1
    nome = str(input('Nome: ')).strip().lower().capitalize()
    alunos.append(nome)
    nota1 = float(input('Nota 1: '))
    alunos.append(nota1)
    nota2 = float(input('Nota 2: '))
    alunos.append(nota2)
    média = (nota1 + nota2)/2
    alunos.append(média)
    alunos.append(count)
    informaçoes.append(alunos[:])
    alunos.clear()
    continuar = ''
    while continuar != "S" and continuar != "N":
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print('\n')
print('=-'*30)
for v in informaçoes:
    #informaçoes.append(count)
    print(f'Aluno: \033[0:32m{v[0]:<30}\033[m Média final = \033[0:33m{v[3]}\033[m')
print('=-'*30)
print('\n')
for v in informaçoes:
    print(f'Aluno {v[4]}: {v[0]}')
continuar = 'S'
print('\n')
while continuar == "S":
    escolha = int(input('Qual aluno deseja ver a nota? Digite: (ex:1,2,3 ...) '))
    print(f'Aluno(a) {informaçoes[escolha - 1][0]}, As notas: \033[0:33mp1 = {informaçoes[escolha - 1][1]} p2 = {informaçoes[escolha - 1][2]}\033[m')
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
