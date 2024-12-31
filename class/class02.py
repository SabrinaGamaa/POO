class Livro():
    def __init__(self, nome_do_livro, codigo):
        self.nome_do_livro = nome_do_livro
        self.codigo = codigo
        print(f'Nome do livro é: {nome_do_livro} e o código é {codigo}')


    def imprime(self, nome_do_livro, codigo):
            print(f'Esse é o livro {nome_do_livro} e o código {codigo}')

livro1 = Livro('O homem aranha', 3873920)
livro2 = Livro('Harry Potter', 389573)
print(livro2.nome_do_livro)
livro1.imprime('O poder do Hábito', 3874202)
