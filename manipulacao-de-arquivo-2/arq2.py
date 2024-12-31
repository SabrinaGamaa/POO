# Abrindo arquivo para gravação
# Se não existir o arquivo, ele mesmo cria e se exister ele sobrepoem
teste_1 = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/arquivo2.txt', 'w')
teste_1.write('Aprendendo a programar em Python. E a metodologia de ensino da Data Science Academy facilita o aprendizado.')
# para fechar o arquivo
teste_1.close()

# teste_2 = open('../DSA/arquivos/arquivo2.txt')
# print(teste_2.read())
# teste_2.close()

teste_3 = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/arquivo2.txt', 'a') # a = append
teste_3.write('\nEstou continuando a jornada de Python no ensino da Data Science Academy.')
teste_3.close()
teste_3 = open('/Users/Sabrina Gama/Downloads/python/POO/manipulacao-de-arquivo-2/arquivos/arquivo2.txt', 'rt')
print(teste_3.read())


