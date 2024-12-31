def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(verificaPar(35))

lista = [2, 4, 6, 3, 5, 2, 7, 3, 14, 64, 23]
print(lista)
ver = filter(verificaPar, lista)
print(f'Os números pares da lista são: {list(ver)}')

print(list(filter(lambda x: x % 1 == 0, lista)))
