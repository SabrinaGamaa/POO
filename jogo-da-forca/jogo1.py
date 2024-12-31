from random import choice

def game():
    print('=-' * 15)
    print('Bem vindo ao jogo da forca!')
    print('Adivinhe a palavra abaixo:')
    lista_de_palavras = ['cimento', 'advogado',	'afta',
                        'alambique',	'alcachofra',	'algarismo',
                        'almanaque',	'almofariz',	'almoxarife',
                        'alquimia', 'altivez',	'sabrina',
                        'amendoim',	'celular',	'amplificar',
                        'ampulheta',	'ansioso',	'aplaudir']

    palavra = choice(lista_de_palavras)
    numero_tentativa = 6
    letras_erradas = []
    letra_descoberta = ['_' for lentra in palavra]
    

    while numero_tentativa > 0:
        print()
        print('Palavra: ',' '.join(letra_descoberta))
        print(f'Tentativas restantes: {numero_tentativa}')
        print(f'Letras erradas:', ' '.join(letras_erradas))
        print('=-' * 15)

        print(palavra)
        tentativa = str(input('Digite uma letra: ')).lower()
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letra_descoberta[index] = letra
                index += 1
        else:
            numero_tentativa -= 1
            letras_erradas.append(tentativa)

        if '_' not in letra_descoberta:
            print('-' * 30)
            print('PARABENS VOCÊ GANHOU!!'.center(30))
            print('-' * 30)
            break
    if '_' in letra_descoberta:
        print(f'Infelizmente você perdeu. A palavra era: {palavra}')

if __name__ =='__main__':
    game()
    print('Estou aprendendo Python!!')
    