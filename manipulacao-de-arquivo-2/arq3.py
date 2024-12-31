abrir = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/salarios.csv', 'rt')
ler = abrir.readlines()
lista_vazia = []

for linha in ler:
    separar_linha = linha.split(',')
    lista_vazia.append(separar_linha)
    print(separar_linha)

count = 0
for linha in ler:
    count += 1
print(f'Tem {count} linhas')

