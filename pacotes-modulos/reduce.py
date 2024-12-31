from functools import reduce

from IPython.display import Image
Image('POO/DSA/arquivos/reduce.png')

lista = [47, 11, 42, 13]

def soma(a, b):
    x = a + b
    return x

# A soma da lista
print(reduce(soma, lista))


print(reduce(lambda x, y: x+y, lista))
#podemos atribuir a expressao lambda a uma variável


max_find = lambda a, b: a if (a > b) else b
# o tipo 
print(type(max_find))
#Aqui vai retornar o maior valor da lista
print(reduce(max_find, lista))

