x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))

# Ela descarta os que não foi possivel fazer a junção
print(list(zip('ABCD', 'xy')))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))

def trocavalores(um, dois):
    fictemp = {}
    print('Vamos fazer um loop')
    for d1key, d2val in zip(um, dois.values()):
        fictemp[d1key] = d2val
    return fictemp


n1 = trocavalores(d1, d2)

print(n1)
