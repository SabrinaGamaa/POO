import csv
with open('POO/manipulacao-de-arquivo-2/numeros.csv', 'w') as arquivo:
    #Criando objeto para a Gravação
    escrever = csv.writer(arquivo)
    escrever.writerow(('nota1', 'nota2', 'nota3'))
    escrever.writerow((63, 87, 92))
    escrever.writerow((61, 79, 78))
    escrever.writerow((28, 84, 43))

# ler o arquivo cvs
with open('POO/manipulacao-de-arquivo-2/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

with open('POO/manipulacao-de-arquivo-2/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)
print('TABELA'.center(15))
for linha in dados[1:]:
    print(f'{linha}')
