#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
p = float(input('Digite o seu peso(kg): '))
a = float(input('Digite a sua altura(m): '))
imc = p/(a*a) #ou a**2
if imc < 18.5:
    print('\033[0:31mAbaixo do peso\033[m. Seu IMC é de {:.2f}'.format(imc))
elif imc < 25:
    print('\033[0:32mPeso ideal\033[m. Seu IMC é de {:.2f}'.format(imc))
elif imc < 30:
    print('\033[0:33mVocê tem sobrepeso\033[m. Seu IMC é de {:.2f}'.format(imc))
elif imc < 40:
    print('\033[0:33mVocê tem Obesidade\033[m. Seu IMC é de {:.2f}'.format(imc))
else:
    print('\033[0:31mVocê tem obesidade mórbida\033[m. Seu IMC é de {:.2f}'.format(imc))