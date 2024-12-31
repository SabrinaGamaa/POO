from random import choice
import os

class JogoForca():  
    palavras = ['cristiano', 'messi', 'neymar', 'vini']
    letras_tentadas = []
    tentativa_restante = 6
    print('-' * 40)
    print('Vamos Jogar o jogo da FORCA!'.center(40))
    print('-' * 40)
    board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

    def __init__(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        palavra_secreta = choice(JogoForca.palavras)
        palavra = ['_' for letra in palavra_secreta]
        
        while JogoForca.tentativa_restante > 0:
            print('-' * 40)
            print(JogoForca.board[6 - JogoForca.tentativa_restante], end=(' -->  '))
            print(' '.join(palavra))
            print('Letras: ',' '.join(JogoForca.letras_tentadas))
            print(f'Tentativas restantes: {JogoForca.tentativa_restante}')
            letra = str(input('Digite a letra: '))
            

            if letra in palavra_secreta:
                print('Sua letra está na palavra secreta')
                index = 0
                for tentativa in palavra_secreta:                        
                    if letra == tentativa:
                        palavra[index] = tentativa
                    index += 1

            elif letra in JogoForca.letras_tentadas:
                print('Essa letra já foi utilizada!') 
               
            else:
                JogoForca.tentativa_restante -= 1
                print(f'Você errou! você tem mais {JogoForca.tentativa_restante} tentativas.')
            
            JogoForca.letras_tentadas.append(letra)

            if '_' not in palavra:
                print('PARABÉNS, Você ganhou!!!')
                break
        if '_' in palavra:
            print(f'Infelimente, você perdeu. A palavra era')
                                

if __name__ == '__main__':
    jogo = JogoForca()
