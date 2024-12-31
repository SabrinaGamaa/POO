class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundida = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')
    #caracteristica:
    # - cor
    # - altura
    # - profundidade
    # - largura
    #
    # métodos do controle remoto:
    # - passar de canal
    # - mexer no volume
    # - abrir a netflix
    # - desligar a tv

controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto.cor)
controle_remoto.passar_canal('+')


print('CONTROLE DOIS'.center(40))
controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')
print(controle_remoto2.altura)
controle_remoto.passar_canal('-')