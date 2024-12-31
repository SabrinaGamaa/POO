abrir = open('../DSA/arquivos/salarios.csv', 'rt')
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

