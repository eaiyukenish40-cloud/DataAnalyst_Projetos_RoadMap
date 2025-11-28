#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n >= 20 or n <= 0:
        n =  int(input('Não foi aceito. Digite um número entre 0 e 20: '))
    print(f'Seu número, {n} por extenso é \033[0:33m{tupla[n]}\033[m')
    decisao = int(input('Deseja continuar? \n1.Sim\n2.Não\n'))
    while decisao != 2 and decisao != 1:
        decisao = int(input('Opção inexistente. Deseja continuar?\n1.Sim\n2.Não\n'))
    if decisao == 2:
        break
