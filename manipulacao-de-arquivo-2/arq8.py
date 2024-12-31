import json
from urllib.request import urlopen
arquivo =  urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
dados = json.loads(arquivo)[0]

#print(dados)

print(f'Título: {dados['title']}')
print(f'URL: {dados['url']}')
print(f'Duração: {dados['duration']}')
print(f'Números de Visualização: {dados['stats_number_of_plays']}')

