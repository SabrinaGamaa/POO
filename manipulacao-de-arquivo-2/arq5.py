import os
#os - operate scient
texto = 'Cientitas de Dados pode ser uma excelente carreira.\n'
texto += 'Esses profissionais precisam saber como programar em Python.\n'
texto += 'E, claro, devem ser proficientes em Data Science.'

#criando um arquivo
# os - bibliotexa, path - caminho, join - juntar
arquivo = open(os.path.join('POO/DSA/arquivos/cientista.txt'), 'w')

for palavra in texto.split():
    arquivo.write(palavra + ' ')
arquivo.close()

arquivo = open('POO/DSA/arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

with open('./POO/DSA/arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))

with open('./POO/DSA/arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:])
arquivo = open('POO/DSA/arquivos/cientista.txt')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
