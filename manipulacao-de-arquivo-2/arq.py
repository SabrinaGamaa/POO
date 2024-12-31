# Abrindo um arquivo para leitura.
#abrir_arquivo = open('C:/Users/Sabrina Gama/Desktop/POO/DSA/arquivos/arquivo1.txt', 'rt')
abrir_arquivo1 = open('../DSA/arquivos/arquivo1.txt')
# descobrir o tipo do arquivo
type(abrir_arquivo1)
print(abrir_arquivo1.read())
# Contar o numero de caracteres
print(f'Tem {abrir_arquivo1.tell()} caracteres dentro desse arquivo.')

# retornar para o inicio do arquivo
print(abrir_arquivo1.seek(0, 0))
# mostra 23 caracteres
print(abrir_arquivo1.read(23))
# Lendo arquivo
print(abrir_arquivo1.read())

