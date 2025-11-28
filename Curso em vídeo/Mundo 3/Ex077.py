#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Palmeiras','Flamengo','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','Sao Paulo','Vasco da Gama','Corinthians','Atletico-MG','Red Bull Bragantino','Ceara','Gremio','Internacional','Vitoria','Santos','Juventude','Fortaleza','Sport')
counta = counte = counti = counto = countu = ''
for palavra in tupla:
    counta = counte = counti = counto = countu = ''
    if 'A' in palavra.upper():
        counta = 'A'
    if 'E' in palavra.upper():
        counte = 'E'
    if 'I' in palavra.upper():
        counti = 'I'
    if 'O' in palavra.upper():
        counto = 'O'
    if 'U' in palavra.upper():
        countu = 'U'
    print(f'A palavra \033[0:32m{palavra}\033[m tem as seguintes vogais \033[0:33m{counta,counte,counti,counto,countu}\033[m.')
