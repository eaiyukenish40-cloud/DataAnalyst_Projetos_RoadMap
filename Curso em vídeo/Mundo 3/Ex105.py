#Faça um programa que tenha uma Função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas, A maior nota,A menor nota, A média da turma, A situação (opcional),Adiciona também as docstrings da Função.
def notas(*n, sit = False):
    """
    :param n: notas que são adicionadas:
    ....
    :param sit: deseja mostrar as notas?
    """
    len(n)
    ranking = dict()
    ranking['Total de notas'] = len(n)
    ranking['Maior nota'] = max(n)
    ranking['Menor nota'] = min(n)
    temp = dict()
    soma = 0
    for c in range(0,len(n)):
        soma += n[c]
    media = (soma/len(n))
    ranking['Média'] = media
    if sit == True:
        if media >= 7:
            ranking['Status média'] = 'Boa'
        elif media >= 5:
            ranking['Status média'] = 'Razoável'
        else:
            ranking['Status média'] = 'Ruim'
    print(ranking)

notas(1,2,4, sit =True)