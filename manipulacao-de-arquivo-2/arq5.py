import os
#os - operate scient
texto = 'Cientitas de Dados pode ser uma excelente carreira.\n'
texto += 'Esses profissionais precisam saber como programar em Python.\n'
texto += 'E, claro, devem ser proficientes em Data Science.'

#criando um arquivo
# os - bibliotexa, path - caminho, join - juntar
arquivo = open(os.path.join('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/cientista.txt'), 'w')

for palavra in texto.split():
    arquivo.write(palavra + ' ')
arquivo.close()

arquivo = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

with open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))

with open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:])
arquivo = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/cientista.txt')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
