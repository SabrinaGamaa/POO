class Carro():
    pass

ferrari = Carro()
print(type(ferrari))

class Estudantes():
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


estudante1 = Estudantes('Maria', '13', 8.4)
print(estudante1.nome)
print(estudante1.idade)
print(estudante1.nota)

