#Faça um programa que leia nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
alunos = []
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Recuperação'
alunos.append(aluno.copy())
print(f'O aluno \033[0:33m{alunos[0]["nome"]}\033[m tem uma média \033[0:33m{alunos[0]["media"]}\033[m e está \033[0:33m{alunos[0]["situacao"]}\033[m!')
