import json
dicionario = {"nome": "Guido van Rossum", "linguagem": "Python", "similar": ["c", "Modula-3", "lisp"], "users": 1000000}

for k, v in dicionario.items():
    print(f"{k}: {v}")

with open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dicionario))

with open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)

print(dados['nome'])
