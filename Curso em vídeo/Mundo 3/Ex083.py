#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
count1 = count2 = temp = 0
erro = 0
expressao = str(input('Digite uma expressão com parentesis: ')).strip()
for c in expressao:
    if c == '(':
        count1 += 1
        lista.append('(')
    if c == ')' and count1 != 0:
        count2 += 1
        lista.append(')')
    elif c == ')' and count1 == 0:
        erro = 1
        break
if count1 != count2:
    print(f'\033[0:31mSua expressão está incorreta\033[m!')
else:
    if erro == 0:
        if count1 == count2:
            for c, v in enumerate(lista):
                if v == '(':
                    temp += 1
                elif v == ')':
                    temp -= 1
                if temp < 0:
                    break
            if temp == 0:
                print('Sua expressão está correta!')
            else:
                print(f'\033[0:31mSua expressão está incorreta\033[m!')
    else:
        print(f'\033[0:31mSua expressão está incorreta\033[m!')

#obs: rever a aula do guanabara. A solução ficou mais enxuta, porém usei o mesmo raciocínio
