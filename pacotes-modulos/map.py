from platform import python_version
def potencia(x):
    return x ** 2
numeros = [1, 2, 3, 4, 5, 6, 7]

numeros_ao_quadrados = list(map(potencia, numeros))
print(numeros_ao_quadrados)

def fahrenheit(t):
    return (float(5)/9 *(t + 32))

def celsius(t):
    return (float(9)/5 * (t - 32))
#criando uma lista
temperaturas = [ 0, 22, 35, 5]

#aplicando a função para cada elemento da lista temperaturas
#Em python, a função map retornar um ITERATOR
lista_fahrenheit = list(map(fahrenheit, temperaturas))
print(f'{lista_fahrenheit}')

lista_celsius = list(map(celsius, temperaturas))
print(lista_celsius)

temp = 0
# for fah in map(celsius, temperaturas)
for fah in lista_celsius:
    print(f'A temperatura de {temperaturas[temp]}° em Fahrennheit é de {lista_fahrenheit[temp]:.2f}°')
    temp += 1
temp = 0
for cel in lista_fahrenheit:
    print(f'A temperatura de {temperaturas[temp]}° em Celsius é de {lista_celsius[temp]:.2f}°')
    temp += 1

b = [2, 4, 5, 3, 6]
list(map(lambda x, y : x+y, temperaturas, b))

