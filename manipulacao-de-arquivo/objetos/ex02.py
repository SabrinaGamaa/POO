class Funcionarios():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listfunc(self):
        print(f'Funcionario {self.nome} tem o salário de R${self.salario:.2f} e o cargo é {self.cargo}')

func1 = Funcionarios('Maria', 20000, 'Cientista de Dados')

print(func1.listfunc())

hasattr(func1, 'nome')
setattr(func1, 'salario', 4500)
func1.listfunc()
getattr(func1, 'salario')
delattr(func1, 'salario')
