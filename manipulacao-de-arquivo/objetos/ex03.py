class Circulo():
    pi = 3.14

    def __init__(self, raio = 5):
        self.raio = raio


    def area(self):
        return (self.raio * self.raio) * Circulo.pi


    def setraio(self, novo_raio):
        self.raio = novo_raio

    def getraio(self):
        return self.raio

circ1 = Circulo(7)
print(f'O raio é: {circ1.getraio()}')
print(f'A area do raio é: {circ1.area()}')
circ1.setraio(9)
print(f'Novo raio é: {circ1.getraio()}')
