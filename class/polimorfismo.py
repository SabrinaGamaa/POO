from time import sleep
class Veiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print('O CARRO está acelerando.')

    def frear(self):
        print('O CARRO está freando.')

class Moto(Veiculo):
    def acelerar(self):
        print('A MOTO está acelerando.')

    def frear(self):
        print('A MOTO está freando')

class Aviao(Veiculo):
    def acelerar(self):
        print('O AVIÃO esta acelerando.')

    def frear(self):
        print('O AVIÃO está freando.')

    def decolando(self):
        print('O AVIÃO está decolando.')


lista_veiculos = [Carro('Porsche', '911 Turbo'), Moto('Honda', 'CB 1000R Black Edition'), Aviao('Boeing', '757')]

for item in lista_veiculos:
    item.acelerar()
    sleep(0.5)
    item.frear()
    sleep(0.5)
    if isinstance(item, Aviao):
        item.decolando()
    print('-' * 15)
