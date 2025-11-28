# 1. Importar a função necessária da biblioteca
from playsound import playsound

# 2. Definir o caminho para o arquivo de áudio
#    Como o arquivo está na mesma pasta, basta o nome dele.
arquivo_mp3 = '01Zer0.mp3'

# 3. Executar a função para tocar o som
print('Tocando a música...')
try:
    playsound(arquivo_mp3)
    print('Música terminou de tocar.')
except Exception as e:
    print(f"Ocorreu um erro ao tentar tocar o áudio: {e}")
    print("Verifique se o nome do arquivo está correto e se ele não está corrompido.")