# Crie um código em Python que testa se o site Pudim está acessível pelo computador usado.
import requests
import urllib # essa é outra biblioteca possível.
import urllib.request
try:
    #resposta = urllib.request.urlopen('http://pudim.com.br')
    resposta = requests.get('http://pudim.com.br', timeout=5)
    if resposta.status_code == 200:
        print('\033[0:32mSite está no ar!\033[m')
    else:
        print(f'Site está inacessíavel. Status {resposta.status_code}')
except:
    print(f'Site está inacessíavel. Status {resposta.status_code}')