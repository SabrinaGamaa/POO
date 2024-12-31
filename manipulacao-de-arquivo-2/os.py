import string
from random import choices

def gerar_senhas(escolha=0):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(choices(caracteres, k=escolha))
    return senha

try:
    while True:
        print('-' * 40)
        print('GERADOR DE SENHAS'.center(40))
        print('-' * 40)
        num_caracteres = int(input('Digite a quantidades de caracteres: '))
        if num_caracteres >= 4:
            print(f'Sua senha é: {gerar_senhas(num_caracteres)}')
            break
        else:
            print('A quantidade de caracteres deve ser 4 ou mais. ')
    print('-' * 40)
except ValueError:
    print('ERRO! Digite um número inteiro.')
except KeyboardInterrupt:
    print('Usuário preferiu não informar um valor.')
except:
    print('Erro ao criar a senha. Por favor, tente novamente.')

