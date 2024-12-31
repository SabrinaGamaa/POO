class Animal():

    def __init__(self, nome):
        print('Animal criado.')
    
    def imprimir(self):
        print('Este é um animal.')

    def comer(self):
        print('Hora de comer.')
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome):
        Animal.__init__(self, nome)
        print('Objeto cachorro criado.')

    def emitir_som(self):
        print('au au')
    

ani1 = Animal('Leao')
ani2 = Cachorro('cachorro')
ani2.emitir_som()
ani1.comer()
